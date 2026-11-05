# AquaFresh Water Delivery Demand Forecasting System

Task 1: Storage decision and synthetic demand data.

## What this project has
- `generate_data.py`: creates 730 days of synthetic daily demand data
- `data.csv`: the generated data (730 rows, one per day)
- `decision-log.md`: why I chose CSV over SQLite

## Columns
date, volume_liters, region, product_type

## Regenerate the data
pip install pandas
python generate_data.py

The random seed is fixed (42), so the volumes are the same every time. Dates are counted back from today.

## Task 2: Baseline forecast
- `baseline.ipynb`: 7-day moving-average baseline (80/20 train/test split by index)
- `predictions.csv`: test predictions (date, actual, baseline_pred)
- `report.md`: MAE and MAPE with a short interpretation

### Run it
Open baseline.ipynb and run all cells.