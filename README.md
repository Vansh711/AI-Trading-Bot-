# AI-Based Reinforcement Learning Trading Bot

## 📌 Project Overview

This project implements an AI-driven stock trading bot using
**Reinforcement Learning (RL)** with the **PPO (Proximal Policy
Optimization)** algorithm.\
The bot is capable of:

-   Learning stock market behaviour using historical data\
-   Fetching **live stock prices** of *Reliance Industries
    (RELIANCE.NS)* via Yahoo Finance\
-   Continuously updating a **real-time price graph**\
-   Predicting **Buy / Sell / Hold** decisions using the trained RL
    model\
-   Acting as the core of a future automated trading system

## 🧠 Problem Statement

The goal is to design an RL-powered automated trading bot that can:

-   Analyze live financial data\
-   Predict optimal trading actions\
-   Continuously update stock trends\
-   Make decisions autonomously without human intervention

## 🛠️ Analysis

### 🔧 Hardware Requirements

-   Intel i5 / AMD Ryzen 5 or higher\
-   8 GB RAM minimum (16 GB recommended)\
-   2--5 GB storage\
-   Optional: NVIDIA GPU

### 💻 Software Requirements

-   Python 3.8+\
-   stable-baselines3, gymnasium, numpy, pandas\
-   matplotlib, yfinance, torch\
-   VS Code / PyCharm

## 🏗️ Design

### 📥 Input Data

-   Live stock data (Open, High, Low, Close, Volume)

### 📊 Observation Space

\[Open, High, Low, Close, Volume\]

### 🎮 Action Space

0 = HOLD\
1 = BUY\
2 = SELL

### 📤 Output

-   RL action\
-   Live graph\
-   Terminal logs

## 🔄 Algorithmic Flow

1.  Collect and preprocess historical data\
2.  Build custom Gym environment\
3.  Train PPO model\
4.  Run live trading\
5.  Update graph in real time\
6.  Display outputs

## 🧩 Modules

### trading_env.py

-   Environment, reward, transitions

### train_model.py

-   PPO training, saving model

### live_trading.py

-   Live price fetch\
-   Model inference\
-   Graph updates

## ✔️ Testing

-   Env reset/step tests\
-   Observation validation\
-   Live data accuracy\
-   Smooth graph rendering

## 🖼️ Output

(Add screenshots)

## 🏁 Conclusion

-   Successful live data processing\
-   RL decision-making\
-   Real-time graph updates

## 🚀 Future Enhancements

-   Zerodha/Upstox integration\
-   Technical indicators\
-   Multi-stock support\
-   Better reward shaping\
-   Dashboard UI
