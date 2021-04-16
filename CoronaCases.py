import pandas as pd
import plotly.express as px

df=pd.read_csv("CoronaCases.csv")
fig=px.bar(df,x="Country",y="No.of Patients",title="Corona Cases In All Countries");
fig.show()
