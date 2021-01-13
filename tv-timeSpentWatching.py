import plotly.express as px
import csv
import numpy as np

with open("Size of TV,_Average time spent watching TV in a week (hours).csv") as csv_file:
    df = csv.DictReader(csv_file)
    fig = px.scatter(df, x="Size of TV", y="\tAverage time spent watching TV in a week (hours)")
    fig.show()

def getDataSource(data_path):
    time_spent_on_watching_tv = []
    size_of_tv = []

    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        
        for row in csv_reader:
            time_spent_on_watching_tv.append(float(row["\tAverage time spent watching TV in a week (hours)"]))
            size_of_tv.append(float(row["Size of TV"]))

    return {"x": size_of_tv, "y": time_spent_on_watching_tv}

def findCorrelation(data_source):
    correlation = np.corrcoef(data_source["x"], data_source["y"])
    print("Correlation between Size of tv and Time spent on watching tv --> ", correlation[0, 1])

def setup():
    data_path = "Size of TV,_Average time spent watching TV in a week (hours).csv"
    data_source = getDataSource(data_path)

    findCorrelation(data_source)

setup()