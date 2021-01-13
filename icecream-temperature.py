import plotly.express as px
import csv
import numpy as np

# with open("Ice-Cream vs Cold-Drink vs Temperature - Ice Cream Sale vs Temperature data.csv") as csv_file:
#     df = csv.DictReader(csv_file)
#     fig = px.scatter(df, x="Temperature", y="Ice-cream Sales( â‚¹ )")
#     fig.show()

def getDataSource(data_path):
    ice_cream_sales = []
    temperature = []

    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        
        for row in csv_reader:
            ice_cream_sales.append(float(row["Ice-cream Sales( â‚¹ )"]))
            temperature.append(float(row["Temperature"]))

    return {"x": temperature, "y": ice_cream_sales}

def findCorrelation(data_source):
    correlation = np.corrcoef(data_source["x"], data_source["y"])
    print("Correlation between Temperature and Ice-cream Sales --> ", correlation[0, 1])

def setup():
    data_path = "Ice-Cream vs Cold-Drink vs Temperature - Ice Cream Sale vs Temperature data.csv"
    data_source = getDataSource(data_path)

    findCorrelation(data_source)

setup()