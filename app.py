# =====================================================
# SALES FORECASTING DASHBOARD
# =====================================================


# Import required libraries

import streamlit as st
import pandas as pd
import plotly.express as px



# =====================================================
# PAGE CONFIGURATION
# =====================================================

# This must be the first Streamlit command

st.set_page_config(
    page_title="Sales Forecasting Dashboard",
    layout="wide"
)



# =====================================================
# DASHBOARD INTRODUCTION
# =====================================================


st.write(
"""
## Project Overview

This dashboard provides sales analysis,
future sales forecasting, anomaly detection,
and product segmentation using machine learning.

The goal is to help businesses understand
past sales patterns and make better decisions
using data-driven insights.
"""
)



# =====================================================
# LOAD DATA FUNCTION
# =====================================================


@st.cache_data
def load_data():

    """
    This function loads all saved CSV files.

    We use cache_data so Streamlit does not
    reload files every time the dashboard refreshes.
    """


    # Monthly sales data

    monthly_sales = pd.read_csv(
        "models/monthly_sales.csv"
    )


    # Model comparison results

    comparison = pd.read_csv(
        "models/model_comparison.csv"
    )


    # Anomaly detection results

    anomaly = pd.read_csv(
        "models/anomaly_results.csv"
    )


    # Product clustering results

    clusters = pd.read_csv(
        "models/product_clusters.csv"
    )


    return (
        monthly_sales,
        comparison,
        anomaly,
        clusters
    )



# Load all datasets

monthly_sales, comparison, anomaly, clusters = load_data()





# =====================================================
# MAIN TITLE
# =====================================================


st.title(
    "Sales Forecasting Dashboard"
)



# Explain final model choice

st.info(
"""
### Final Model Selection

XGBoost was selected as the final forecasting model.

Reason:
XGBoost achieved better performance compared with
SARIMA and Prophet based on MAE, RMSE, and MAPE metrics.
"""
)





# =====================================================
# SIDEBAR NAVIGATION
# =====================================================


page = st.sidebar.selectbox(

    "Select Dashboard Section",

    [
        "Sales Overview",
        "Forecast Explorer",
        "Anomaly Report",
        "Product Segments"
    ]

)





# =====================================================
# PAGE 1
# SALES OVERVIEW
# =====================================================


if page == "Sales Overview":


    st.header(
        "Sales Overview"
    )


    st.write(
    """
    This section shows historical sales performance
    and model comparison results.
    """
    )


    # Calculate total sales

    total_sales = (
        monthly_sales["Sales"]
        .sum()
    )


    # KPI card

    st.metric(

        "Total Sales",

        f"${total_sales:,.2f}"

    )



    # Sales trend visualization


    fig = px.line(

        monthly_sales,

        x="Date",

        y="Sales",

        title="Monthly Sales Trend"

    )


    st.plotly_chart(

        fig,

        use_container_width=True

    )



    # Model comparison


    st.subheader(

        "Forecast Model Performance"

    )


    st.write(
    """
    The table compares forecasting models using:

    - MAE
    - RMSE
    - MAPE

    Lower values indicate better model performance.
    """
    )


    st.dataframe(

        comparison,

        use_container_width=True

    )



    st.success(
    """
    XGBoost was selected as the production forecasting
    model because it provided the best accuracy.
    """
    )






# =====================================================
# PAGE 2
# FORECAST EXPLORER
# =====================================================


elif page == "Forecast Explorer":


    st.header(

        "Future Sales Forecast"

    )


    st.write(
    """
    Select a category or region to view
    future sales predictions.
    """
    )



    # User selection


    option = st.selectbox(

        "Choose Forecast Type",

        [

            "Furniture",

            "Technology",

            "Office Supplies",

            "West Region",

            "East Region"

        ]

    )



    # Connect selection with files


    forecast_files = {


        "Furniture":

        "models/furniture_forecast.csv",



        "Technology":

        "models/technology_forecast.csv",



        "Office Supplies":

        "models/office_forecast.csv",



        "West Region":

        "models/west_forecast.csv",



        "East Region":

        "models/east_forecast.csv"

    }




    # Load selected forecast


    forecast = pd.read_csv(

        forecast_files[option]

    )



    st.subheader(

        f"{option} Forecast"

    )



    # Show forecast values


    st.dataframe(

        forecast,

        use_container_width=True

    )



    # Forecast graph


    fig = px.line(

        forecast,

        x="Date",

        y="Forecast",

        title=f"{option} Future Sales Prediction"

    )


    st.plotly_chart(

        fig,

        use_container_width=True

    )







# =====================================================
# PAGE 3
# ANOMALY REPORT
# =====================================================


elif page == "Anomaly Report":



    st.header(

        "Sales Anomaly Detection"

    )


    st.write(
    """
    Anomalies represent unusual sales periods.

    These were detected using:
    
    - Isolation Forest
    - Z-score method

    They help businesses investigate
    unexpected sales changes.
    """
    )



    st.subheader(

        "All Results"

    )


    st.dataframe(

        anomaly,

        use_container_width=True

    )



    st.subheader(

        "Detected Anomalies Only"

    )



    anomaly_only = anomaly[

        anomaly["IF_Label"]

        ==

        "Anomaly"

    ]



    st.dataframe(

        anomaly_only,

        use_container_width=True

    )







# =====================================================
# PAGE 4
# PRODUCT SEGMENTATION
# =====================================================


elif page == "Product Segments":



    st.header(

        "Product Demand Segmentation"

    )



    st.write(
    """
    KMeans clustering is used to group products
    according to their sales behaviour.

    This helps identify different product demand patterns.
    """
    )



    # Show cluster data


    st.dataframe(

        clusters,

        use_container_width=True

    )



    # Count products per cluster


    cluster_count = (

        clusters["Cluster"]

        .value_counts()

        .reset_index()

    )



    cluster_count.columns = [

        "Cluster",

        "Number of Products"

    ]



    # Cluster chart


    fig = px.bar(

        cluster_count,

        x="Cluster",

        y="Number of Products",

        title="Products in Each Cluster"

    )



    st.plotly_chart(

        fig,

        use_container_width=True

    )