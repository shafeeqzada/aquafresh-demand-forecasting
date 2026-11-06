# Baseline Report: 7-day Moving Average

- Train rows: 584
- Test rows: 146
- MAE: 85.19 liters
- MAPE: 53.55 %

## Interpretation
- MAE = 85.19 liters: on average, the baseline's prediction is about 85 liters away from the actual daily demand.
- MAPE = 53.55%: on average, the prediction is off by about 54% of the actual value, which is a high error.
- Why the error is high: the product type (small, medium, large) and region change every day, so demand jumps between about 73 and 388 liters. A 7-day average stays between about 124 and 290 liters and cannot follow these jumps.
- This is only a baseline. A better model should get lower MAE and MAPE than these numbers.
