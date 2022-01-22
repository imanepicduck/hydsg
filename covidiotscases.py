import pandas as pd  
import plotly.express as px   
data = 1

df = pd.read_csv(data.csv)
fig = px.scatter(df, x="date", y="cases", color="country")
fig.show()