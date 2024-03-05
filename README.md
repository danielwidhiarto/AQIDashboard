# Air Quality Index Dashboard

This dashboard is built using Streamlit and displays various visualizations related to air quality index data from two locations: Changping and Wanliu.

## Quick Access to Graphs

- [Area Plot for PM2.5](#area-plot-for-pm25)
- [Bar Plot for Average PM2.5](#bar-plot-for-average-pm25)
- [Histogram for NO2](#histogram-for-no2)
- [Scatter Plot for PM2.5 vs O3](#scatter-plot-for-pm25-vs-o3)
- [Box Plot for PM10](#box-plot-for-pm10)

## Setup Enviroment
   ```sh
   conda create --name main-ds python=3.9
   conda activate main-ds
   pip install numpy pandas scipy matplotlib seaborn jupyter streamlit babel  

## Run Streamlit App
 ```sh
   streamlit run dashboard.py

