# import library
import streamlit as st
from PIL import Image

# icon page
st.set_page_config(
    page_title="introduction",
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
st.markdown("<h1 style='text-align:center'>RenewRide</h1>", unsafe_allow_html=True)

# Sub header 1
st.subheader('Pendahuluan')

# isi pendahuluan
with st.container():
    col1, col2 = st.columns(2)
    with col1:
        st.write('Dalam era teknologi dan keberlanjutan, minat terhadap kendaraan ramah lingkungan semakin melonjak. Pertumbuhan penjualan kendaraan listrik yang kian pesat menciptakan peluang besar bagi konsumen. Tapi, beralih ke mobil listrik bukan keputusan mudah. Info yang minim dan kendala pembelian menjadi tantangan utamanya. Dengan itu, kami hadir dengan solusi lengkap: informasi jelas dan fitur trade-in untuk mempermudah beralih ke kendaraan listrik')
    with col2:
        introduction_img = Image.open(r"./images/Pendahuluan.jpg")
        st.image(introduction_img, caption='EV Car')

# Sub header 1
st.subheader('Pernyataan masalah')

# isi pernyataan masalah
with st.container():
    col3, col4 = st.columns(2)
    with col3:
        earth = Image.open(r"./images/bumi.jpg")
        st.image(earth, caption='Global Warming')
    with col4:
        st.write('Dalam konteks pertumbuhan urbanisasi dan ketergantunganmasyarakat pada kendaraan bermotor, permasalahan polusiudara semakin menjadi ancaman serius. Terutama, sektortransportasi menjadi penyumbang emisi dari polusi udarayang merugikan kesehatan manusia dan mengancamkeberlanjutan lingkungan. Kendaraan konvensional, denganemisinya, memperparah kualitas udara, menghasilkan dampaknegatif yang terasa di lingkungan perkotaan. Adanya lonjakanemisi karbon dari transportasi ini juga memberikansumbangan signifikan terhadap perubahan iklim global. Oleh karena itu, dibutuhkan solusi inovatif yang tidak hanyamengatasi kendala perpindahan ke kendaraan listrik tetapijuga berkontribusi pada upaya mitigasi polusi udara dan pengurangan emisi karbon secara keseluruhan.')


# anggota kelompok
st.markdown("<h3 style='text-align:center'>Anggota Kelompok</h3>", unsafe_allow_html=True)

# Data Analytics
with st.container():
    col5, col6, col7 = st.columns(3)
    with col5:
        st.markdown("<h5 style='text-align:center'>Data Analytics</h5>", unsafe_allow_html=True)
        st.markdown("""<ol>
                            <li>Nesya Syahira</li>
                            <li>Nabila Agustina Cahyani Putri</li>
                            <li>Muhammad Indra Buana</li>
                            <li>Aqyla Riva Nisafitria</li>
                        </ol>""", 
                    unsafe_allow_html=True)
    with col6:
        st.markdown("<h5 style='text-align:center'>Product Management</h5>", unsafe_allow_html=True)
        st.markdown("""<ol>
                            <li>Salsabila Putri Ardefa</li>
                            <li>Zuvika Nandra Sabriyani</li>
                            <li>Dwi Oktavia</li>
                        </ol>""", 
                    unsafe_allow_html=True)
    with col7:
        st.markdown("<h5 style='text-align:center'>UI/UX Design</h5>", unsafe_allow_html=True)
        st.markdown("""<ol>
                            <li>Tasya Nursipa</li>
                            <li>Renaldo Rahmat Kurniawan</li>
                            <li>Sandrina Putri Daneswari</li>
                        </ol>""", 
                    unsafe_allow_html=True)