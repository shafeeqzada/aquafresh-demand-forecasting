# AquaFresh Water Delivery Demand Forecasting System

![CI](https://github.com/shafeeqzada/aquafresh-demand-forecasting/actions/workflows/ci.yml/badge.svg)

## Project overview
This project forecasts daily water delivery demand. It generates 730 days of synthetic demand data, builds a 7-day moving-average baseline and a Prophet model with a rolling back-test, analyses errors by region and product type, and shows everything in a Streamlit dashboard with a PDF report download.

**Live dashboard:** [https://aquafresh-demand-forecasting.streamlit.app/]

## Setup
1. Install Python 3.11 and Git.
2. Download the project: `git clone https://github.com/shafeeqzada/aquafresh-demand-forecasting.git`
3. Open the folder and run: `pip install -r requirements.txt`

## Regenerate the data
`python generate_data.py`
This creates `data.csv` (730 rows, one per day). The random seed is fixed, so results are repeatable.

## Run the dashboard locally
`streamlit run app.py`
Open http://localhost:8501

## Run with Docker
1. Install Docker Desktop.
2. Build: `docker build -t aquafresh-demand-forecasting .`
3. Run: `docker run -p 8501:8501 aquafresh-demand-forecasting`
4. Open http://localhost:8501

Or use the ready image from Docker Hub: `docker run -p 8501:8501 YOUR_DOCKERHUB_USERNAME/aquafresh-demand-forecasting:latest`

## CI (GitHub Actions)
On every push to `main`, GitHub builds the Docker image and pushes it to Docker Hub. The badge above shows whether the last build passed.

## How to update the forecast
Replace or regenerate `data.csv`, re-run the notebooks (`baseline.ipynb`, `prophet_model.ipynb`, `error_analysis.ipynb`) to refresh the CSV files, then push to GitHub. The Docker image and the Streamlit app update automatically.

## Security note
No passwords, tokens or API keys are stored in this repository. Docker Hub credentials are kept in GitHub Secrets (`DOCKERHUB_USERNAME`, `shafeeq787`) and are never written in code or documentation. Do not commit secrets to the repo.

# Project tasks

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


## Task 5: Streamlit dashboard and PDF report
- `app.py`: dashboard with sidebar filters (region, product type, date range), actual vs Prophet line chart, error bar chart, and a PDF download button
- `requirements.txt`: packages for Streamlit Cloud

### Run it
pip install -r requirements.txt
streamlit run app.py


Note: each region/product combination has only a few test days (each date has one region and one product), so charts and metrics for a single segment are based on few points.


## Task 6: Docker, CI and deployment
- `Dockerfile`: builds the image and runs the app on port 8501
- `.dockerignore`: files Docker should skip
- `.github/workflows/ci.yml`: builds the image and pushes it to Docker Hub on every push
- Live dashboard and run instructions: see the sections at the top of this README