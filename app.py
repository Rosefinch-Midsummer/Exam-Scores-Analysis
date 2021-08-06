import streamlit as st                                                  
import yfinance as yf   

ticker_dict={'Google':'GOOGL', 'Microsoft':'MSFT', 'Apple':'AAPL'}  

#add a selectbox to the sidebar
add_selectbox= st.sidebar.selectbox('Which company would you like to be displayed?', (list(ticker_dict.keys())))

st.write(f"""
# Simple Stock Price App 
Shown are the stock closing prices and volumes of {add_selectbox}!
""")

# define the ticker symbol
tickerSymbol = ticker_dict[add_selectbox]
# 'MSFT'  'GOOGL'  'AAPL'

#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)  
# get the historical prices for this ticker

tickerDf=tickerData.history(start='2011-6-22', end='2021-6-22')     

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)
