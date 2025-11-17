import numpy as np
import gymnasium as gym
from gymnasium import spaces


class TradingEnv(gym.Env):
    metadata = {"render_modes": ["human"]}

    def __init__(self, df):
        super(TradingEnv, self).__init__()

        # Store dataset (works for historical + live)
        self.df = df
        self.max_steps = len(df) - 1 if df is not None else 1

        # Environment state
        self.current_step = 0
        self.balance = 100000
        self.shares = 0
        self.initial_balance = 100000

        # Observation: [Open, High, Low, Close, Volume]
        self.observation_space = spaces.Box(
            low=-np.inf, high=np.inf, shape=(5,), dtype=np.float32
        )

        # Action space → 0 = Hold, 1 = Buy, 2 = Sell
        self.action_space = spaces.Discrete(3)

    # ----------------------------------------------------------------------
    def _get_obs(self):
        """Returns observation for PPO."""
        row = self.df.iloc[self.current_step]

        obs = np.array([
            float(row["Open"]),
            float(row["High"]),
            float(row["Low"]),
            float(row["Close"]),
            float(row["Volume"])
        ], dtype=np.float32)

        return obs

    # ----------------------------------------------------------------------
    def reset(self, seed=None, options=None):
        super().reset(seed=seed)

        self.current_step = 0
        self.balance = 100000
        self.shares = 0

        return self._get_obs(), {}

    # ----------------------------------------------------------------------
    def step(self, action):
        price = float(self.df["Close"].iloc[self.current_step])

        prev_value = self.balance + self.shares * price

        # ACTIONS ------------------------------------------------------------
        if action == 1:  # BUY
            if self.balance >= price:
                self.shares += 1
                self.balance -= price

        elif action == 2:  # SELL
            if self.shares > 0:
                self.shares -= 1
                self.balance += price

        # NEXT STEP ----------------------------------------------------------
        self.current_step += 1
        done = self.current_step >= self.max_steps

        new_price = float(self.df["Close"].iloc[self.current_step - 1])
        new_value = self.balance + self.shares * new_price

        reward = new_value - prev_value

        obs = self._get_obs()

        return obs, reward, done, False, {
            "portfolio_value": new_value
        }

    # ----------------------------------------------------------------------
    def render(self):
        print(
            f"Step: {self.current_step} | Balance: {self.balance:.2f} | Shares: {self.shares}"
        )
