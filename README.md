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


## Task 3: Prophet model with rolling back-test
- `prophet_model.ipynb`: fits Prophet on the train data and runs a rolling back-test (7-day horizon, history grows with each fold)
- `prophet_model.pkl`: saved Prophet model
- `backtest_results.csv`: date, actual, prophet_pred for the test period
- `comparison.md`: baseline vs Prophet MAE and MAPE

### Run it
pip install prophet
Open prophet_model.ipynb and run all cells.

## Task 4: Error analysis by region and product
- `error_analysis.ipynb`: merges Prophet predictions with region and product_type, computes error per segment
- `error_by_region.csv`, `error_by_product.csv`: MAE and MAPE per segment
- `region_error.png`, `product_error.png`: bar charts
- `analysis.md`: which segments have the highest errors

### Run it
Open error_analysis.ipynb and run all cells.