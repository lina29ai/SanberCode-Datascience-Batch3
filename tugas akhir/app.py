import os
import pandas as pd
import streamlit as st

data_dummy = {
    'precision': [0.98, 0.93, 0.95, 0.94],
    'recall': [0.97, 0.95, 0.97, 0.96],
    'f1-score': [0.97, 0.94, 0.96, 0.95],
    'support': [50, 50, 50, 150]
}

index_dummy = ['setosa', 'versicolor', 'virginica', 'accuracy']
df_dummy = pd.DataFrame(data_dummy, index=index_dummy)

st.title("Dashboard Klasifikasi")
 
st.write("Tabel Hasil Klasifikasi:")
st.dataframe(df_dummy)

st.bar_chart(df_dummy[['precision', 'recall', 'f1-score']])
