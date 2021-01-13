import plotly.express as px
import csv
import numpy as np

with open("Student Marks vs Days Present.csv") as csv_file:
    df = csv.DictReader(csv_file)
    fig = px.scatter(df, x="Days Present", y="Marks In Percentage")
    fig.show()

def getDataSource(data_path):
    marks_in_percentage = []
    days_present = []

    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        
        for row in csv_reader:
            marks_in_percentage.append(float(row["Marks In Percentage"]))
            days_present.append(float(row["Days Present"]))

    return {"x": days_present, "y": marks_in_percentage}

def findCorrelation(data_source):
    correlation = np.corrcoef(data_source["x"], data_source["y"])
    print("Correlation between Days present and Marks in percentage --> ", correlation[0, 1])

def setup():
    data_path = "Student Marks vs Days Present.csv"
    data_source = getDataSource(data_path)

    findCorrelation(data_source)

setup()