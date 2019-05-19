import pandas as pd

data = pd.read_csv("bikeshare.csv")
X = data[["rowid",
"date",
"season",
"year",
"month",
"hour",
"holiday",
"weekday",
"workingday",
"weather",
"temp",
"feelslike",
"humidity",
"windspeed",
"casual",
"registered"
]]

y = data["riders"]

print(y)
