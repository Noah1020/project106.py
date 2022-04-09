import numpy as np
import plotly.express as px
import csv

def getDataSource(filename):
    days=[]
    marks=[]
    with open(filename)as f:
        reader = csv.DictReader(f)
        for a in reader:
            days.append(float(a["Days Present"]))
            marks.append(float(a["Marks In Percentage"]))
    return{"x":days, "y":marks}

def plotfigure():
    with open("MarksvsPresent.csv")as f:
        reader = csv.DictReader(f)
        fig = px.scatter(reader, x="Days Present", y="Marks In Percentage")
        fig.show()


datasorce = getDataSource("MarksvsPresent.csv")
correlation = np.corrcoef(datasorce["x"], datasorce["y"])
print(correlation[0,1])
plotfigure()