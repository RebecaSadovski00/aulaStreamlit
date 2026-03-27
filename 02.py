import streamlit as st
import pandas as pd
import yfinance as yf

@st.cache_data
def carregar_dados(empresa):
    dados_acao = yf.Ticker(empresa)
    cotacoes_acao = dados_acao.history(start="2010-01-01", end="2024-07-01")
    return cotacoes_acao

dados = carregar_dados("ITUB4.SA")
print(dados)

st.write("""
# App preço de ações
O gráfico abaixo representa a evolução do preço das ações do Itaú 
""") #markdown

st.write(dados)

st.write("""
# Fim do app""")
