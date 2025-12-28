# Time Series Sales Forecasting

## Overview
This project analyzes multi‑year daily retail sales data and produces simple visual forecasts to support inventory and planning decisions. The focus is on turning raw transactional data into clear daily and monthly time‑series views plus a baseline 6‑month demand forecast using Python.[web:55][web:85]

## Dataset
- Source: Store Sales – Time Series Forecasting (Kaggle competition).[web:55]
- Description: Daily sales for multiple stores and product families over several years (3M+ rows of transactional data).[web:55][web:12]
- Link: https://www.kaggle.com/c/store-sales-time-series-forecasting

> The raw `train.csv` file is not included in this repository. Download it from Kaggle and place it in the `DATA/RAW` folder as described below.[web:55]

## Project Structure

time-series-sales-forecasting/
├── DATA/
│ └── RAW/
│ └── train.csv # Kaggle Store Sales training data (not tracked)
├── portfolio.py # Main script to generate the combined figure
├── portfolio_complete.png # Output image (daily, monthly, forecast)
├── daily_sales.csv # Aggregated daily sales (generated)
└── README.md


## Methods
1. Data loading and aggregation  
   - Load `train.csv` from the Kaggle Store Sales dataset.[web:55]  
   - Aggregate raw rows to obtain total daily sales across all stores and product families.  
   - Derive monthly sales by grouping daily data by year‑month.

2. Visualization  
   - Daily sales plot to show long‑term trend and short‑term volatility.  
   - Monthly sales plot to highlight growth and seasonality.  
   - Simple 6‑month forecast curve based on recent average sales as a baseline demand forecast.[web:24][web:34]

3. Baseline forecasting  
   - Compute recent average daily sales and extend it forward for 6 months (180 days).  
   - Use this as an interpretable baseline that can later be replaced or compared with ARIMA/SARIMA/Prophet models.[web:21][web:24]

## How to Run

### 1. Install requirements

pip install pandas matplotlib


### 2. Set up data
1. Download `train.csv` from the Kaggle Store Sales – Time Series Forecasting competition.[web:55]  
2. Create the folder structure:

DATA/
└── RAW/
└── train.csv
3. Place `train.csv` inside `DATA/RAW`.

### 3. Generate outputs
From the project root, run:

python portfolio.py

This will:
- Load the Kaggle data from `DATA/RAW/train.csv`.  
- Aggregate to daily (and monthly) sales.  
- Generate a combined figure with:
  - Daily Sales Trend
  - Monthly Sales
  - 6‑Month Forecast  
- Save the figure as `portfolio_complete.png` and the aggregated data as `daily_sales.csv`.

## Results

The final figure (`portfolio_complete.png`) contains three panels:

- Daily Sales Trend – shows overall growth in daily sales and variability over time.  
- Monthly Sales – shows total sales per month, making trend and seasonality easier to interpret.  
- 6‑Month Forecast – provides a simple baseline forecast based on recent sales levels for planning.

Example metrics to fill in after running:
- Average daily sales: `<value>`  
- Peak month by total sales: `<YYYY-MM>`  
- Simple 6‑month forecast total: `<value>`  

## Next Steps
Planned improvements:
- Add ARIMA/SARIMA models and evaluate accuracy using MAPE/RMSE.
- Compare baseline vs model‑based forecasts.  
- Build an interactive dashboard (Power BI/Tableau) using the aggregated daily/monthly data for stakeholders.[web:5][web:11]

## Tech Stack
- Language: Python  
- Libraries: Pandas, Matplotlib  
- Data: Kaggle Store Sales – Time Series Forecasting (train.csv)
