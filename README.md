# AquaFresh Water Delivery Demand Forecasting System

Task 1: Storage decision and synthetic demand data.

## What this project has
- `generate_data.py`: creates 730 days of synthetic daily demand data
- `data.csv`: the generated data (6,570 rows = 730 days x 3 regions x 3 product types)
- `decision-log.md`: why I chose CSV over SQLite

## Columns
date, volume_liters, region, product_type

## Regenerate the data
pip install pandas
python generate_data.py

The random seed is fixed (42), so the volumes are the same every time. Dates are counted back from today.