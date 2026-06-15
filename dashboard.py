import psycopg2
import streamlit as st
import pandas as pd

connection = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="aranel33",
    port="5432"
)

df = pd.read_sql_query("SELECT * FROM exchange_rates", connection)
# st.write(df)

currencies = df['target_currency'].unique()
selected_currency = st.selectbox("Select the currency you want to track", currencies)
filtered_df = df[df['target_currency'] == selected_currency]
st.write(filtered_df)

st.line_chart(data=filtered_df, x="currency_date", y="rate")