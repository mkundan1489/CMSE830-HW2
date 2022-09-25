import streamlit as st
import seaborn as sns
import pandas as pd
import plotly.express as pl

iris_data = sns.load_dataset("iris")
st.write("""
# 3d Scattered plot between sepal length, sepal width and petal width of iris dataset.
""")
fig = pl.scatter_3d(iris_data, x='sepal_length', y='sepal_width', z='petal_width',
              color='species')
fig.show()