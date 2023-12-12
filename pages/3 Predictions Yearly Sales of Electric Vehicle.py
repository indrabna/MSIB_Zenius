# import library
import streamlit as st
import pandas as pd
import plotly.express as px

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
st.markdown("<h1 style='text-align:center'>Predictions Yearly Sales of Electric Vehicle</h1>", unsafe_allow_html=True)

# load dataset
sales_by_country = pd.read_csv('https://raw.githubusercontent.com/Nabilaagustina/Zenius/main/dataset_final_project/sales.csv')
predict_sales = pd.read_csv('https://raw.githubusercontent.com/Nabilaagustina/Zenius/main/dataset_final_project/prediction_sales.csv')
predict_sales['Year'] = pd.to_datetime(predict_sales['Year'], format='%Y-%m-%d')
predict_sales['Year'] = predict_sales['Year'].dt.strftime('%Y')

with st.container():
    col1, col2= st.columns(2)
    with col1:
        with st.container():
            col3, col4= st.columns(2)
            with col3:
                total_sales = float(pd.Series(sales_by_country['total_sales']).sum())
                st.metric(label="💰 Total Prediction Sales",value=f"{total_sales:,.0f}")
            with col4:
                total_data = float(sales_by_country.shape[0])
                st.metric(label="Total Data",value=f"{total_data:,.0f}")
        st.markdown("<h4 style='text-align:center'>Metode Prediksi</h4>", unsafe_allow_html=True)
        st.write('Kelompok Kami menggunakan metode prediksi dengan menerapkan algoritma machine learning dengan jenis regresi yaitu model algoritma linear regression.')
    with col2:
        st.markdown("<h4 style='text-align:center'>Sumber Data</h4>", unsafe_allow_html=True)
        st.markdown("""
                    Jumlah data: 9542 baris data.<br>
                    Sumber data: https://www.kaggle.com/datasets/edsonmarin/historic-sales-of-electric-vehicles. <br>
                    Fitur untuk prediksi:
                    <ol>
                        <li>Type.</li>
                        <li>Powertrain.</li>
                        <li>Year.</li>
                    </ol>""", 
                    unsafe_allow_html=True)

st.markdown("<h4 style='text-align:center'>Jumlah penjualan tahun 2010 - 2020 dengan detail berdasarkan jenis kendaraan dan jenis mesin</h4>", unsafe_allow_html=True)

fig = px.bar(sales_by_country, x='powertrain', y='total_sales', color='mode')

# Customize the chart if needed
fig.update_layout(barmode='group')

# Display the chart using Streamlit
st.plotly_chart(fig)

st.write('Berdasarkan diagram barplot di atas prediksi jumlah penjualan terbanyak dengan jenis kendaraan mobil dan jenis mesin BEV.')

st.markdown("<h4 style='text-align:center'>Jumlah penjualan tahun 2010 - 2020 berdasarkan jenis kendaraan</h4>", unsafe_allow_html=True)

fig = px.pie(sales_by_country, values='total_sales', names='mode', labels={'total_sales': 'Percentage'}, color_discrete_sequence=px.colors.qualitative.Set3, hole=0.4)

# Customizing layout
fig.update_traces(textinfo='percent+label', hoverinfo='label+percent')
fig.update_layout(margin=dict(l=20, r=20, t=30, b=0), height=300)  # Sesuaikan ukuran plot

# Display the plot using Streamlit
st.plotly_chart(fig)

st.write('Berdasarkan diagram doughnut chart di atas prediksi jumlah penjualan terbanyak dengan jenis kendaraan mobil.')

st.markdown("<h4 style='text-align:center'>Jumlah penjualan tahun 2010 - 2020</h4>", unsafe_allow_html=True)

df_year = sales_by_country.groupby('year').agg({'total_sales':sum}).reset_index()
st.line_chart(df_year, x="year", y="total_sales")

# Header 2
st.markdown("<h1 style='text-align:center'>Hasil prediksi</h1>", unsafe_allow_html=True)

st.markdown("<h4 style='text-align:center'>Prediksi jumlah penjualan (2024-2028) dengan detail berdasarkan jenis kendaraan dan jenis mesin</h4>", unsafe_allow_html=True)

fig = px.bar(predict_sales, x='Powertrain', y='Prediction Sales', color='Mode')

# Customize the chart if needed
fig.update_layout(barmode='group')

# Display the chart using Streamlit
st.plotly_chart(fig)

st.write('Berdasarkan diagram barplot di atas prediksi jumlah penjualan terbanyak dengan jenis kendaraan mobil dan jenis mesin BEV.')

st.markdown("<h4 style='text-align:center'>Prediksi jumlah penjualan (2024-2028) berdasarkan jenis kendaraan</h4>", unsafe_allow_html=True)

fig = px.pie(predict_sales, values='Prediction Sales', names='Mode', labels={'Prediction Sales': 'Percentage'}, color_discrete_sequence=px.colors.qualitative.Set3, hole=0.4)

# Customizing layout
fig.update_traces(textinfo='percent+label', hoverinfo='label+percent')
fig.update_layout(margin=dict(l=20, r=20, t=30, b=0), height=300)  # Sesuaikan ukuran plot

# Display the plot using Streamlit
st.plotly_chart(fig)

st.write('Berdasarkan diagram doughnut chart di atas prediksi jumlah penjualan terbanyak dengan jenis kendaraan mobil.')

st.markdown("<h4 style='text-align:center'>Prediksi jumlah penjualan (2024-2028)</h4>", unsafe_allow_html=True)

df_year = predict_sales.groupby('Year').agg({'Prediction Sales':sum}).reset_index()
st.line_chart(df_year, x="Year", y="Prediction Sales")

st.markdown("<h5>Evaluate model:</h5>", unsafe_allow_html=True)
st.markdown("""<ol>
                    <li>MAPE: 23.379229391881804</li>
                    <li>MAE:4447.140498494322</li>
                    <li>MSE: 30940440.10590139</li>
                    <li>R-squared: 0.9199664062322683</li>
                </ol>""", 
            unsafe_allow_html=True)