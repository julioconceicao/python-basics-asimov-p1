import streamlit as st
import pandas as pd
import plotly.express as px

#f = filter
#df = dataframe
#p = price

#BODY LAYOUT
st.set_page_config(layout="wide")

#DATAFRAME INGEST
df_reviews = pd.read_csv("./datasets/customer reviews.csv")
df_top100_books = pd.read_csv("./datasets/Top-100 Trending Books.csv")

#FILTER SIDEBAR
p_max = df_top100_books["book price"].max()
p_min = df_top100_books["book price"].min()
f_price = st.sidebar.slider("Select books by price", p_min, p_max, p_max)

#DATAFRAME VIEW
df_books = df_top100_books[df_top100_books["book price"] <= f_price]
df_books 

#FIGURE ANALYSIS
fig = px.bar(df_books["year of publication"].value_counts())
fig2 = px.histogram(df_books["book price"])

col1, col2 = st.columns(2)

col1.plotly_chart(fig)
col2.plotly_chart(fig2)