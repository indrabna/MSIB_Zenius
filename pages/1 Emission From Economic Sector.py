# import library
import streamlit as st
import pandas as pd
import plotly.express as px

# icon page
st.set_page_config(
    page_title="Emission From Economic Sector",
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

# Header
st.markdown("<h1 style='text-align:center'>Emission From Economic Sector</h1>", unsafe_allow_html=True)

# load dataset
emissions_2021 = pd.read_csv('https://raw.githubusercontent.com/Nabilaagustina/Zenius/main/dataset_final_project/2021%20U.S.%20GHG%20Emissions%20by%20Sector.csv')
emissions_1990_2021 = pd.read_csv('https://raw.githubusercontent.com/Nabilaagustina/Zenius/main/dataset_final_project/U.S.%20GHG%20Emissions%201990-2021.csv')
GHG_emissions = pd.read_csv('https://raw.githubusercontent.com/Nabilaagustina/Zenius/main/dataset_final_project/Transportation%20Sector%20GHG%20Emissions%20Based%20on%20Vehicle%20Type.csv')
co2_reduced = pd.read_csv('https://raw.githubusercontent.com/Nabilaagustina/Zenius/main/dataset_final_project/CO2%20that%20Can%20Be%20Red_uced.csv')
petroleum_reduced = pd.read_csv('https://raw.githubusercontent.com/Nabilaagustina/Zenius/main/dataset_final_project/Gasoline%20that%20Can%20Be%20Reduced.csv')

# sub header
st.markdown("<h4 style='text-align:center'>2021 U.S. GHG Emissions by Sector</h4>", unsafe_allow_html=True)

fig = px.pie(emissions_2021, values='2021', names='U.S. Emissions by Economic Sector, MMT CO2 eq.', labels={'2021': 'Percentage'}, color_discrete_sequence=px.colors.qualitative.Set3)

# Customizing layout
fig.update_traces(textinfo='percent+label', hoverinfo='label+percent')
fig.update_layout(margin=dict(l=20, r=20, t=30, b=0), height=300)  # Sesuaikan ukuran plot

# Display the plot using Streamlit
st.plotly_chart(fig)

# Interpretasi U.S. Emissions by Economic Sector in 2021
st.write('Sector transportasi menyumbang porsi terbesar (29%) dari total emisi GRK AS pada tahun 2021.')

st.markdown("<h4 style='text-align:center'>U.S. GHG Emissions 1990-2021</h4>", unsafe_allow_html=True)
# linechart U.S. GHG Emissions 1990-2021
st.line_chart(emissions_1990_2021, x="Year", y="Emissions")

# Interpretasi U.S. GHG Emissions 1990-2021
st.write('Emisi dari sektor transportasi cenderung meningkat dari tahun 1990-2020, sempat terjadi penurunan dari tahun 2019-2020 dikarenakan covid kemudian kembali meningkat.')

# Header 2
st.markdown("<h1 style='text-align:center'>Transportation Sector GHG Emissions Based on Vehicle Type</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align:center'>(Comparison of CO2 Produced)</h4>", unsafe_allow_html=True)

# isi bagian 2
with st.container():
    col1, col2 = st.columns(2)
    with col1:
        st.bar_chart(GHG_emissions, x="Tipe Kendaraan", y="Rata-rata CO2 yang dihasilkan")
    with col2:
        st.markdown("<h4 style='text-align:center'>Perbandingan Keseluruhan</h4>", unsafe_allow_html=True)
        st.write('Kendaraan listrik (Electric Vehicle) menunjukkan angka emisi CO2 yang paling rendah, yaitu 88,7. Ini mencerminkan keunggulan EV dalam mengurangi emisi gas rumah kaca, karena EV tidak menghasilkan emisi langsung saat beroperasi dan kinerja lebih ramah lingkungan.')

        st.markdown("<h4 style='text-align:center'>Electric Vehicles atau Conventional Vehicles?</h4>", unsafe_allow_html=True)
        st.write('Dari segi emisi CO2, Electric Vehicle (EV) memiliki dampak lingkungan yang lebih rendah dibandingkan dengan kendaraan berbahan bakar fosil seperti Internal Combustion Engine (ICE) dan Liquified Petroleum Gas (LPG).')

# Header 3
st.markdown("<h1 style='text-align:center'>Potential Reduction in CO2 Emissions and Gasoline Consumption by Electric Vehicles</h1>", unsafe_allow_html=True)

# isi bagian 3
with st.container():
    col3, col4 = st.columns(2)
    with col3:
        st.markdown("<h4 style='text-align:center'>CO2 that Can Be Red​uced</h4>", unsafe_allow_html=True)
        st.bar_chart(co2_reduced, x="Tipe Kendaraan", y="Mean Annual GHG Emissions Reductions (MT CO2e)")
        st.markdown("<h5 style='text-align:center'>Baik BEV maupun PHEV memiliki potensi yang signifikan untuk mengurangi emisi CO2 dibandingkan dengan kendaraan konvensional yang menggunakan mesin pembakaran internal konvensional.</h5>", unsafe_allow_html=True)
        st.write('Pengurangan emisi CO2 yang signifikan dari kendaraan listrik dapat memberikan kontribusi positif terhadap solusi perubahan iklim melalui pengurangan emisi CO2 yang berasal dari sektor transportasi, yang seringkali menjadi penyumbang besar terhadap polusi udara di perkotaan.')
    with col4:
        st.markdown("<h4 style='text-align:center'>Gasoline that Can Be Reduced</h4>", unsafe_allow_html=True)
        st.bar_chart(petroleum_reduced, x="Tipe Kendaraan", y="Mean Annual Petroleum Reductions (gallons)")
        st.markdown("<h5 style='text-align:center'>BEV menunjukkan dampak yang lebih besar dalam mengurangi penggunaan bensin karena mereka sepenuhnya bergantung pada tenaga listrik untuk pengoperasian normal.</h5>", unsafe_allow_html=True)
        st.write('Pengurangan penggunaan bensin oleh kendaraan listrik dapat membantu mengurangi emisi gas rumah kaca dan polusi udara, membantu mengurangi ketergantungan pada sumber daya fosil dan memberikan keuntungan ekonomi melalui penghematan biaya bahan bakar, sehingga memberikan kontribusi positif pada keberlanjutan dan kesehatan lingkungan.')