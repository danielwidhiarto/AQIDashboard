import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def combine_data(changping_file, wanliu_file):
    df_changping = pd.read_csv(changping_file)
    df_wanliu = pd.read_csv(wanliu_file)
    df_changping['location'] = 'Changping'
    df_wanliu['location'] = 'Wanliu'
    
    df_combined = pd.concat([df_changping, df_wanliu], ignore_index=True)
    
    return df_combined

changping_file = os.path.join("..", "data", "changping.csv")
wanliu_file = os.path.join("..", "data", "wanliu.csv")

df = combine_data(changping_file, wanliu_file)

st.title('Air Quality Index Dashboard')
st.set_option('deprecation.showPyplotGlobalUse', False)

option = st.sidebar.selectbox(
    'Pilih Grafik',
    ('Area Plot untuk PM2.5', 'Bar Plot untuk Rata-rata PM2.5', 'Histogram untuk Tingkat NO2', 
     'Scatter Plot untuk PM2.5 vs O3', 'Box Plot untuk PM10')
)

if option == 'Area Plot untuk PM2.5':
    st.subheader('Area Plot untuk PM2.5')
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=df, x='hour', y='PM2.5', hue='location', ci=None)
    plt.fill_between(df['hour'], df['PM2.5'], alpha=0.3)
    plt.xlabel('Hour')
    plt.ylabel('PM2.5 Level')
    plt.title('Area Plot of PM2.5')
    st.pyplot()

elif option == 'Bar Plot untuk Rata-rata PM2.5':
    st.subheader('Bar Plot untuk Rata-rata PM2.5')
    average_pm25 = df.groupby('location')['PM2.5'].mean().reset_index()
    plt.figure(figsize=(8, 6))
    sns.barplot(data=average_pm25, x='location', y='PM2.5')
    plt.xlabel('Location')
    plt.ylabel('Average PM2.5 Level')
    plt.title('Bar Plot of Average PM2.5')
    st.pyplot()

elif option == 'Histogram untuk Tingkat NO2':
    st.subheader('Histogram untuk Tingkat NO2')
    plt.figure(figsize=(10, 6))
    sns.histplot(data=df, x='NO2', bins=30, kde=True, hue='location', multiple='stack')
    plt.xlabel('NO2 Level')
    plt.ylabel('Frequency')
    plt.title('Histogram of NO2 Level')
    st.pyplot()

elif option == 'Scatter Plot untuk PM2.5 vs O3':
    st.subheader('Scatter Plot untuk PM2.5 vs O3')
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df, x='PM2.5', y='O3', hue='location')
    plt.xlabel('PM2.5 Level')
    plt.ylabel('O3 Level')
    plt.title('Scatter Plot of PM2.5 vs O3')
    st.pyplot()

elif option == 'Box Plot untuk PM10':
    st.subheader('Box Plot untuk PM10')
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=df, x='location', y='PM10')
    plt.xlabel('Location')
    plt.ylabel('PM10 Level')
    plt.title('Box Plot of PM10')
    st.pyplot()