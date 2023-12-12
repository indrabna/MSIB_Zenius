# import library
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import geopandas as gpd

# icon page
st.set_page_config(
    page_title="Yearly Sales of  Electric Vehicle (2010-2020)",
    page_icon= "🌍",
)

# Logo 
def add_logo():
    st.markdown(
        """
        <style>
            [data-testid="stSidebarNav"] {
                background-image: url('https://i.pinimg.com/564x/5d/68/dc/5d68dcb900a65caf1286d4024a105c73.jpg');
                background-repeat: no-repeat;
                padding-top: 120px;
                background-position: 20px 20px;
                background-size: 250px 200px;  
            }
            [data-testid="stSidebarNav"]::before {
                content: "RenewRide";
                display: block;
                margin-left: 20px;
                margin-top: 20px;
                font-size: 30px;
                position: relative;
                top: 100px;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

add_logo()

# Header 1
st.markdown("<h1 style='text-align:center'>Yearly Sales of  Electric Vehicle (2010-2020)</h1>", unsafe_allow_html=True)

# load dataset
sales_by_country = pd.read_csv('https://raw.githubusercontent.com/Nabilaagustina/Zenius/main/dataset_final_project/sales.csv')
sales_by_country2 = sales_by_country.copy()

# list data
list_region = list(sales_by_country['region'].unique())
list_year = list(sales_by_country['year'].unique())

world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

with st.container():
    col1, col2= st.columns(2)
    with col1:
        country_filter = st.multiselect('Select Region', list_region)
    with col2:
        year_filter = st.multiselect('Select Year', list_year)

if country_filter and year_filter:
    filtered_data = sales_by_country[(sales_by_country['year'].isin(year_filter)&sales_by_country['region'].isin(country_filter))]
elif year_filter:
    filtered_data = sales_by_country[sales_by_country['year'].isin(year_filter)]
elif country_filter:
    filtered_data = sales_by_country[sales_by_country['region'].isin(country_filter)]
else:
    filtered_data = sales_by_country.copy()

# total sales
total_sales = float(pd.Series(filtered_data['total_sales']).sum())

st.metric(label="💰 Total Sales",value=f"{total_sales:,.0f}")

# Membuat kamus untuk pemetaan region
region_mapping = {
    'EU27': 'Europe',
    'United Kingdom': 'Europe',
    'Italy': 'Europe',
    'India': 'Asia',
    'Japan': 'Asia',
    'Brazil': 'South America',
    'Austria': 'Europe',
    'Korea': 'Asia',
    'Europe': 'Europe',
    'Netherlands': 'Europe',
    'Denmark': 'Europe',
    'Iceland': 'Europe',
    'France': 'Europe',
    'Belgium': 'Europe',
    'USA': 'North America',
    'Germany': 'Europe',
    'Poland': 'Europe',
    'China': 'Asia',
    'Other Europe': 'Europe',
    'Portugal': 'Europe',
    'Spain': 'Europe',
    'Norway': 'Europe',
    'Canada': 'North America',
    'Sweden': 'Europe',
    'New Zealand': 'Oceania',
    'Chile': 'South America',
    'Australia': 'Oceania',
    'Switzerland': 'Europe',
    'Rest of the world': 'Seven seas (open ocean)',
    'Finland': 'Europe',
    'Mexico': 'North America',
    'Israel': 'Asia',
    'Turkiye': 'Asia',
    'South Africa': 'Africa',
    'Greece': 'Europe'
}

data = filtered_data.copy()

st.markdown("<h4 style='text-align:center'>Electric Vehicle Sales by Country</h4>", unsafe_allow_html=True)
# Mengganti nilai kolom 'region' dengan menggunakan map
data['region'] = data['region'].map(region_mapping)
data = data.groupby('region').agg({'total_sales':sum})

data = world.merge(pd.DataFrame(data), how='left', left_on='continent', right_on='region')

# Plot the map with sales data
fig, ax = plt.subplots(figsize=(10, 6))
data.plot(column='total_sales', cmap='OrRd', linewidth=0.8, ax=ax, edgecolor='0.8', legend=True)
ax.set_axis_off()

# Display the map in Streamlit
st.pyplot(fig)

st.markdown("<h4 style='text-align:center'>Electric Vehicle Sales by Powertrain</h4>", unsafe_allow_html=True)

fig = px.pie(filtered_data, values='total_sales', names='powertrain', labels={'total_sales': 'Percentage'}, color_discrete_sequence=px.colors.qualitative.Set3)

# Customizing layout
fig.update_traces(textinfo='percent+label', hoverinfo='label+percent')
fig.update_layout(margin=dict(l=20, r=20, t=30, b=0), height=300)  # Sesuaikan ukuran plot

# Display the plot using Streamlit
st.plotly_chart(fig)

df_top5_countries = sales_by_country.copy()
df_top5_countries = df_top5_countries.groupby('region').agg({'total_sales':sum})
df_top5_countries = df_top5_countries.sort_values(by='total_sales', ascending=False).head(5).reset_index()

df_top5_year = sales_by_country.copy()
df_top5_year = df_top5_year.groupby('year').agg({'total_sales':sum})
df_top5_year = df_top5_year.sort_values(by='total_sales', ascending=False).head(5).reset_index()

df_mode_year_sales = sales_by_country.copy()
df_mode_year_sales = df_mode_year_sales.groupby(['mode', 'year']).agg({'total_sales':sum}).reset_index()

with st.container():
    col3, col4 = st.columns(2)
    with col3:
        st.markdown("<h4 style='text-align:center'>Top 5 Countries with the Highest Electric Vehicle Sales</h4>", unsafe_allow_html=True)
        st.bar_chart(df_top5_countries, x="region", y="total_sales")
        st.write('Eropa, khususnya Prancis dan Jerman, memiliki tingkat adopsi kendaraan listrik yang tinggi.')
    with col4:
        st.markdown("<h4 style='text-align:center'>Top 5 Year with the Highest Electric Vehicle Sales</h4>", unsafe_allow_html=True)
        st.bar_chart(df_top5_year, x="year", y="total_sales")
        st.write('Penjualan kendaraan listrik mengalami peningkatan yang signifikan selama lima tahun terakhir, dengan puncaknya terjadi pada tahun 2020 dengan penjualan sebanyak 184.868 unit.')

# Header 2
st.markdown("<h4 style='text-align:center'>Time Series of Electric Vehicle Sales by Type</h4>", unsafe_allow_html=True)

# linechart Time Series of Electric Vehicle Sales by Type
fig2 = px.line(df_mode_year_sales, x="year", y="total_sales", color="mode", line_group='mode', markers=True)

# Display the chart using Streamlit
st.plotly_chart(fig2)

st.write('Mobil listrik menunjukkan tren penjualan yang dominan sepanjang periode dan terus meningkat hingga 2019. Namun terjadi penurunan dalam penjualan pada tahun 2020 yang mungkin dipengaruhi oleh faktor seperti pandemi COVID-19 terkait penurunan perilaku konsumen dan industri otomotif secara keseluruhan.')