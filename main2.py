import csv 
import pandas as pd
import plotly.graph_objects as go
df=pd.read_csv("data.csv")
newdf=df.loc[df["student_id"]=="TRL_xsl"]
print(newdf.groupby("level")["attempt"].mean())
graph=go.Figure(go.Bar(
    x=newdf.groupby("level")["attempt"].mean(),
    y=["level1","level2","level3","level4"],orientation="h"
))
graph.show()