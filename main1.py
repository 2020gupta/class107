import csv
import pandas as pd
import plotly.graph_objects as go
df=pd.read_csv("data.csv")
print(df.groupby("student_id")["attempt"].mean())
graph=go.Figure(go.Bar(
    x=df.groupby("student_id")["attempt"].mean(),
    y=["t1","t2","t3","t4","t5","t6","t7","t8","t9","t10","t11","t12"],orientation="h"
    
))
graph.show()