import streamlit as st

st.title("Menghitung  :blue[Volume Tabung] :rocket:")

r = st.number_input("Masukan Jari-Jari (cm): ",0)
r = st.number_input("Masukan Tinggi (cm): ",0)
if  st.button("Hitung Volume", type="primary):
v = math.pi*(r**2)*t
st.success(f'Volume tabung adalah (v:,2f)')
