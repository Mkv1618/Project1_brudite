import csv
import json

data=[]

with open("excsv.csv", "r") as f:
    data = list(csv.reader(f, delimiter=','))

names=[i[0] for i in data]
mail=[i[1] for i in data]

data= dict(zip(names, mail))

with open("exjson.json", "w") as f:
    json.dump(data, f)
