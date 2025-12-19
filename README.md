# Air Quality Index Dashboard

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://danielwidhiarto-aqidashboard.streamlit.app/)

A comprehensive air quality monitoring dashboard built with Streamlit that visualizes Air Quality Index (AQI) data from two locations in Beijing: Changping and Wanliu. The dashboard provides interactive visualizations for various air pollutants including PM2.5, PM10, NO2, and O3.

## 📊 Live Demo

Check out the live dashboard: [https://danielwidhiarto-aqidashboard.streamlit.app/](https://danielwidhiarto-aqidashboard.streamlit.app/)

## 🌟 Features

- **Interactive Visualizations**: Multiple chart types to analyze air quality data
- **Multi-location Comparison**: Compare air quality between Changping and Wanliu
- **Real-time Data**: Dashboard fetches data directly from GitHub repository
- **Multiple Pollutant Tracking**: Monitor PM2.5, PM10, NO2, and O3 levels
- **User-friendly Interface**: Easy navigation with sidebar selection menu

## 📈 Available Visualizations

1. **Area Plot for PM2.5**: Hourly PM2.5 levels across different locations
2. **Bar Plot for Average PM2.5**: Comparative average PM2.5 levels by location
3. **Histogram for NO2 Levels**: Distribution of NO2 concentrations
4. **Scatter Plot for PM2.5 vs O3**: Relationship between PM2.5 and Ozone levels
5. **Box Plot for PM10**: Statistical distribution of PM10 levels

## 🗂️ Project Structure

```
AQIDashboard/
├── dashboard/
│   ├── dashboard.py          # Main Streamlit application
│   └── all_data.csv          # Combined dataset
├── data/
│   ├── changping.csv         # Changping location data
│   └── wanliu.csv            # Wanliu location data
├── notebook.ipynb            # Data analysis notebook
├── requirements.txt          # Python dependencies
├── README.md                 # Project documentation
└── url.txt                   # Live dashboard URL
```

## 🚀 Getting Started

### Prerequisites

- Python 3.9 or higher
- pip or conda package manager

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/danielwidhiarto/AQIDashboard.git
   cd AQIDashboard
   ```

2. **Create a virtual environment** (using conda)

   ```bash
   conda create --name aqi-dashboard python=3.9
   conda activate aqi-dashboard
   ```

   Or (using venv)

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

   Or install manually:

   ```bash
   pip install streamlit pandas matplotlib seaborn numpy requests
   ```

### Running the Dashboard

1. **Navigate to the dashboard directory**

   ```bash
   cd dashboard
   ```

2. **Run the Streamlit app**

   ```bash
   streamlit run dashboard.py
   ```

3. **Access the dashboard**

   The dashboard will automatically open in your default browser at `http://localhost:8501`

## 📊 Data Analysis

The project includes a Jupyter notebook (`notebook.ipynb`) for exploratory data analysis. To run the notebook:

```bash
jupyter notebook notebook.ipynb
```

## 🔧 Technologies Used

- **Streamlit**: Web application framework
- **Pandas**: Data manipulation and analysis
- **Matplotlib**: Data visualization
- **Seaborn**: Statistical data visualization
- **NumPy**: Numerical computing
- **Requests**: HTTP library for fetching data

## 📦 Dependencies

All required packages are listed in `requirements.txt`. Key dependencies include:

- streamlit==1.31.1
- pandas==2.2.1
- matplotlib==3.8.3
- seaborn==0.13.2
- numpy==1.26.4
- requests==2.31.0

## 🌍 Data Sources

The dashboard uses air quality data from two monitoring stations in Beijing:

- **Changping District**: Northern Beijing suburban area
- **Wanliu**: Urban area in Haidian District

Data includes measurements of:

- PM2.5 (Fine Particulate Matter)
- PM10 (Particulate Matter)
- NO2 (Nitrogen Dioxide)
- O3 (Ozone)
- Hourly timestamps

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the MIT License.

## 👤 Author

**Daniel Widhiarto**

- GitHub: [@danielwidhiarto](https://github.com/danielwidhiarto)
- Dashboard: [AQIDashboard](https://danielwidhiarto-aqidashboard.streamlit.app/)

## 🙏 Acknowledgments

- Air quality data sourced from Beijing environmental monitoring stations
- Built with Streamlit's amazing framework
- Visualization powered by Matplotlib and Seaborn

---

**Note**: This dashboard is for educational and informational purposes. For official air quality information, please refer to your local environmental agency.
