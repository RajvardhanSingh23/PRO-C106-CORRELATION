import numpy as np 
import csv
import pandas as pd 
import plotly.express as px
with open("cups_of_coffee_vs_hours_of_sleep.csv") as f:
    df = csv.DictReader(f)
    fig = px.scatter(df, x="Coffee in ml", y="sleep in hours")
    fig.show()
def getDataSource(data_path):
    coffeeInMl = []
    sleepInHours = []
    with open(data_path) as csvFile:
        csvReader = csv.DictReader(csvFile)
        for row in csvReader:
            coffeeInMl.append(float(row["Coffee in ml"]))
            sleepInHours.append(float(row["sleep in hours"]))
    return {"x":coffeeInMl, "y":sleepInHours}
def findCorrelation(dataSource):
    correlation = np.corrcoef(dataSource["x"], dataSource["y"])
    print("Correlation Between Coffee in ml vs sleep in hours:- ", correlation[0,1])
def setUp():
    data_path = "cups_of_coffee_vs_hours_of_sleep.csv"
    dataSource = getDataSource(data_path)
    findCorrelation(dataSource)
setUp()
