import streamlit as st
import pandas as pd
import yfinance as yf

st.title("Meu primeiro app.")
st.write("Funcionando!")

texto = st.text_input("Digite uma palavra:")
if texto:
    st.write("Você digitou:", texto)