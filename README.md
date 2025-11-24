# AI-Based Reinforcement Learning Trading Bot

## 📌 Project Overview
This project implements an AI-driven stock trading bot using **Reinforcement Learning (RL)** with the **PPO (Proximal Policy Optimization)** algorithm.  
The bot is capable of:

- Learning stock market behaviour using historical data  
- Fetching **live stock prices** of *Reliance Industries (RELIANCE.NS)* via Yahoo Finance  
- Continuously updating a **real-time price graph**  
- Predicting **Buy / Sell / Hold** decisions using the trained RL model  
- Acting as the core of a future automated trading system  

---

## 🧠 Problem Statement
The goal is to design an RL-powered automated trading bot that can:

- Analyze live financial data  
- Predict optimal trading actions  
- Continuously update stock trends  
- Make decisions autonomously without human intervention  

The challenge lies in enabling real-time analysis, prediction, and visualization while working with fast-changing NSE stock data.

---

## 🛠️ Analysis

### 🔧 Hardware Requirements
- Processor: Intel i5 / AMD Ryzen 5 or higher  
- RAM: **8 GB minimum**, 16 GB recommended  
- Storage: 2–5 GB free  
- Optional: NVIDIA GPU for faster model training  

### 💻 Software Requirements
- OS: Windows / macOS / Linux  
- Python **3.8+**  
- Virtual environment: `venv`  
- Required Libraries:
  - `stable-baselines3` (PPO)
  - `gymnasium`
  - `numpy`, `pandas`
  - `matplotlib`
  - `yfinance`
  - `torch`
- IDE: VS Code / PyCharm

---

## 🏗️ Design

### 📥 Input Data
- Live stock data from Yahoo Finance  
- Historical dataset (AAPL or RELIANCE) for training  

### 📊 Observation Space
Normalized numerical features:
