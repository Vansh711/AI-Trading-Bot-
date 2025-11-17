import matplotlib.pyplot as plt
from nsetools import Nse
import time
import numpy as np

# --- STOCK DETAILS ---
STOCK = "RELIANCE"

# --- NSE API ---
nse = Nse()

# --- Matplotlib Setup ---
plt.ion()
fig, ax = plt.subplots(figsize=(10,5))

times = []
prices = []

line, = ax.plot(times, prices, marker='o')

ax.set_title(f"Live Price: {STOCK}")
ax.set_xlabel("Time (seconds)")
ax.set_ylabel("Price (INR)")
ax.grid(True)

# --- SIMPLE AI LOGIC (Dummy for Now) ---
def get_signal(price_history):
    if len(price_history) < 3:
        return "HOLD"
    if price_history[-1] > price_history[-3]:
        return "BUY"
    if price_history[-1] < price_history[-3]:
        return "SELL"
    return "HOLD"


# --- LIVE LOOP ---
start_time = time.time()

while True:
    quote = nse.get_quote(STOCK)

    if quote is None or "lastPrice" not in quote:
        print("⚠️ Could not fetch data. Retrying...")
        time.sleep(3)
        continue

    price = float(quote["lastPrice"])
    current_time = round(time.time() - start_time)

    print(f"⏱ {current_time}s | ₹{price}")

    # --- Update arrays ---
    times.append(current_time)
    prices.append(price)

    # --- Update Graph ---
    line.set_xdata(times)
    line.set_ydata(prices)

    ax.relim()
    ax.autoscale_view()

    plt.draw()
    plt.pause(0.01)

    # --- Get BUY/SELL/HOLD ---
    decision = get_signal(prices)
    print("📢 AI Signal:", decision)

    time.sleep(3)
