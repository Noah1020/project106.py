import numpy as np
import plotly.express as px
import csv

def getDataSource(filename):
    Coffee=[]
    Sleep=[]
    with open(filename)as f:
        reader = csv.DictReader(f)
        for a in reader:
            Coffee.append(float(a["Coffee in ml"]))
            Sleep.append(float(a["sleep in hours"]))
    return{"x":Coffee, "y":Sleep}

def plotfigure():
    with open("CoffeevsSleep.csv")as f:
        reader = csv.DictReader(f)
        fig = px.scatter(reader, x="Coffee in ml", y="sleep in hours")
        fig.show()


datasorce = getDataSource("CoffeevsSleep.csv")
correlation = np.corrcoef(datasorce["x"], datasorce["y"])
print(correlation)
plotfigure()