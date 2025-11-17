import gymnasium as gym
import numpy as np
import pandas as pd
from stable_baselines3 import PPO
from trading_env import TradingEnv
import yfinance as yf

# Load training data (Reliance Daily Data)
print("📥 Downloading Reliance data...")
df = yf.download("RELIANCE.NS", start="2020-01-01", end="2024-12-31")
df = df[["Open", "High", "Low", "Close", "Volume"]].dropna()

# Train Environment
env = TradingEnv(df=df)

# PPO Model
model = PPO("MlpPolicy", env, verbose=1)

print("🚀 Training started...")
model.learn(total_timesteps=50_000)

# Save model
model.save("../models/ppo_trading_model")
print("✅ Training complete! Saved as ppo_trading_model.zip")
