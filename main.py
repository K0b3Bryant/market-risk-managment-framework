# main.py
import pandas as pd
from utils import validate_inputs, calculate_portfolio_metrics, calculate_risk_measures
from config import CONFIG

def main():
    # Example input data: Replace with actual data or dynamic input handling
    portfolio_data = pd.DataFrame({
        'Date': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04'],
        'Asset1_Price': [100, 101, 102, 103],
        'Asset1_Position': [1.0, 0.5, -1.0, 0.0],
        'Asset2_Price': [200, 202, 201, 203],
        'Asset2_Position': [0.0, 1.0, 0.5, -0.5]
    })

    try:
        validated_data = validate_inputs(portfolio_data)

        # Calculate portfolio metrics
        portfolio_metrics = calculate_portfolio_metrics(validated_data)
        print("\nPortfolio Metrics:")
        print(portfolio_metrics)

        # Calculate risk measures
        risk_measures = calculate_risk_measures(portfolio_metrics)
        print("\nRisk Measures:")
        print(risk_measures)

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
