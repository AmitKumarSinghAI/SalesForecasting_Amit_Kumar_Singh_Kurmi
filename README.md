# Sales Forecasting and Demand Intelligence System

An end-to-end machine learning project that analyzes retail sales data, forecasts future demand, detects unusual sales behavior, and segments products based on demand patterns.

## Project Objective

The objective of this project is to help a retail company improve inventory planning and business decisions by:

- Understanding historical sales trends
- Predicting future sales demand
- Comparing forecasting models
- Detecting unusual sales activities
- Segmenting products based on demand behavior
- Providing insights through an interactive Streamlit dashboard

---

# Project Workflow

Data Collection
→ Data Cleaning
→ Exploratory Data Analysis
→ Feature Engineering
→ Time Series Analysis
→ Forecasting Models
→ Model Evaluation
→ Anomaly Detection
→ Product Segmentation
→ Streamlit Deployment

---

# Dataset

Superstore Sales Dataset

Main features:

- Order Date
- Ship Date
- Customer Information
- Region
- Category
- Sub-Category
- Product Information
- Sales

---

# Project Structure

```
SalesForecasting_Project

├── analysis.ipynb
├── app.py
├── train.csv
├── requirements.txt
├── summary.pdf
├── charts/
└── models/
    ├── monthly_sales.csv
    ├── model_comparison.csv
    ├── anomaly_results.csv
    ├── product_clusters.csv
    ├── furniture_forecast.csv
    ├── technology_forecast.csv
    ├── office_forecast.csv
    ├── west_forecast.csv
    └── east_forecast.csv
```

---

# Technologies Used

## Data Analysis
- Python
- Pandas
- NumPy

## Visualization
- Matplotlib
- Seaborn
- Plotly

## Machine Learning
- Scikit-learn
- XGBoost

## Forecasting
- SARIMAX
- Prophet

## Deployment
- Streamlit Community Cloud

---

# Implementation Details

## 1. Exploratory Data Analysis

Performed:

- Data loading
- Data cleaning
- Missing value analysis
- Duplicate checking
- Date feature engineering
- Sales trend analysis
- Category and regional analysis
- Seasonal analysis

---

## 2. Time Series Analysis

Performed:

- Monthly sales aggregation
- Trend visualization
- Seasonal decomposition
- Stationarity checking using ADF test

---

## 3. Forecasting Models

Implemented models:

### SARIMAX
Traditional statistical forecasting model.

### Prophet
Used for trend and seasonal forecasting.

### XGBoost
Machine learning forecasting model using:

- Lag features
- Rolling averages
- Time-based features

Models were evaluated using:

- MAE
- RMSE
- MAPE

The best performing model was selected for future forecasting.

---

# Category and Region Forecasting

Forecasts were generated for:

Categories:
- Furniture
- Technology
- Office Supplies

Regions:
- West
- East

---

# Anomaly Detection

Implemented:

## Isolation Forest

Machine learning based anomaly detection.

## Z-score Method

Statistical method to identify unusual sales values.

Detected anomalies were analyzed to understand possible business causes.

---

# Product Demand Segmentation

Products were grouped using clustering techniques.

The segmentation helps identify:

- High demand products
- Medium demand products
- Low demand products

This supports better inventory strategies.

---

# Streamlit Dashboard

The dashboard contains four sections:

## Sales Overview

Includes:

- Total sales KPI
- Monthly sales trend
- Model comparison

## Forecast Explorer

Includes:

- Category and region forecast selection
- Future sales visualization

## Anomaly Report

Includes:

- Detected unusual sales activities
- Anomaly results

## Product Segments

Includes:

- Cluster visualization
- Product demand groups

---

# Running the Project Locally

Clone repository:

```bash
git clone <repository-url>
```

Create environment:

```bash
python -m venv venv
```

Activate:

```bash
venv\Scripts\activate
```

Install libraries:

```bash
pip install -r requirements.txt
```

Run dashboard:

```bash
streamlit run app.py
```

---

# Deployment

The application is deployed using Streamlit Community Cloud.

Steps:

1. Upload project to GitHub
2. Connect repository with Streamlit Cloud
3. Select app.py
4. Deploy application

---

# Business Impact

This system helps organizations:

- Improve inventory planning
- Reduce stock shortage risk
- Identify abnormal sales events
- Understand product demand
- Make data-driven decisions

---

# Future Improvements

Possible improvements:

- Real-time sales data integration
- Automatic model retraining
- Advanced deep learning forecasting
- Cloud database integration

---

# Author

Amit Kumar Singh
