# Risk Management Framework

## Overview
This framework is designed for portfolio risk management, supporting multiple assets and providing comprehensive risk measures. It includes tools for calculating portfolio metrics, Value at Risk (VaR), Expected Shortfall (ES), Monte Carlo simulation, and visualizations.

---

## Key Features
1. **Portfolio Metrics**:
   - Calculates weighted portfolio returns based on asset positions and prices.
   - Computes portfolio-level statistics such as cumulative returns and volatility.

2. **Risk Measures**:
   - **Value at Risk (VaR)**: Estimates the worst expected loss at a specified confidence level.
   - **Expected Shortfall (ES)**: Calculates the average loss beyond the VaR threshold.
   - **Drawdown Analysis**: Measures the maximum drawdown and duration.

3. **Monte Carlo Simulation**:
   - Simulates portfolio return paths over a given horizon with multiple iterations.

4. **Stress Testing**:
   - Evaluates portfolio risk under predefined market shocks.

5. **Correlation Analysis**:
   - Computes the correlation matrix of asset returns to assess diversification benefits.

6. **Visualizations**:
   - Cumulative returns plot.
   - Monte Carlo simulation paths.
   - Correlation matrix heatmap.

---

## Project Structure
- **main.py**: Entry point for the framework. Validates inputs, calculates metrics, and runs risk measures.
- **utils.py**: Core functions for risk calculations, simulations, and visualizations.
- **config.py**: Centralized configuration for key parameters.

---

## Usage
1. Prepare your input data as a DataFrame with the following columns:
   - `Date`: The date for each observation (format specified in `CONFIG['date_format']`).
   - `{Asset}_Price`: Price of each asset.
   - `{Asset}_Position`: Position size (float) for each asset.

2. Update the `CONFIG` file as needed:
   - `assets`: List of asset names (e.g., `['Asset1', 'Asset2']`).
   - `lag`: Number of periods to lag positions (default is `1`).
   - `confidence_level`: Confidence level for risk measures (default is `0.95`).

3. Run `main.py` to execute the analysis and view results:
   - Portfolio metrics (e.g., returns, drawdown).
   - Risk measures (e.g., VaR, ES, volatility).
   - Visualizations for cumulative returns, Monte Carlo paths, and correlation matrix.

---
