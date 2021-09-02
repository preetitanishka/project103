import pandas as pd
import plotly.express as px
import csv

df=pd.read_csv("Copy+of+data+-+data.csv")
fig=px.scatter(df, x="date", y="cases", color="country")
fig.show()
