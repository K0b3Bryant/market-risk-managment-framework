import pandas as pd
import numpy as np
from config import CONFIG

def validate_inputs(data: pd.DataFrame):
    # Ensure required columns exist
    required_columns = [col for asset in CONFIG['assets'] for col in [f'{asset}_Price', f'{asset}_Position']]
    required_columns.insert(0, 'Date')
    
    if not all(col in data.columns for col in required_columns):
        raise ValueError(f"Data must contain the following columns: {required_columns}")

    # Check date formats and ensure consistency
    data['Date'] = pd.to_datetime(data['Date'], format=CONFIG['date_format'])

    # Check for missing values
    if data.isnull().values.any():
        raise ValueError("Data contains missing values.")

    return data

def calculate_portfolio_metrics(data: pd.DataFrame):
    portfolio_returns = []
    for asset in CONFIG['assets']:
        data[f'{asset}_Returns'] = data[f'{asset}_Price'].pct_change()
        data[f'{asset}_Weighted_Returns'] = data[f'{asset}_Returns'] * data[f'{asset}_Position'].shift(CONFIG['lag'])
        portfolio_returns.append(data[f'{asset}_Weighted_Returns'])

    # Portfolio Returns
    data['Portfolio_Returns'] = sum(portfolio_returns)

    return data[['Date', 'Portfolio_Returns'] + \
                [f'{asset}_Returns' for asset in CONFIG['assets']] + \
                [f'{asset}_Weighted_Returns' for asset in CONFIG['assets']]]

def calculate_risk_measures(data: pd.DataFrame):
    returns = data['Portfolio_Returns'].dropna()

    # Value at Risk (VaR)
    var_95 = np.percentile(returns, 100 * (1 - CONFIG['confidence_level']))

    # Expected Shortfall (ES)
    es_95 = returns[returns <= var_95].mean()

    # Portfolio Volatility
    volatility = returns.std()

    return {
        'VaR (95%)': var_95,
        'Expected Shortfall (95%)': es_95,
        'Volatility': volatility
    }
