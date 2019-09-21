import pandas as pd

data = pd.read_csv("bikeshare.csv")


features = [

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
"registered",
"riders",
]
X = data[features]
y = data

from yellowbrick.features import Rank1D

# Instantiate the 1D visualizer with the Sharpiro ranking algorithm
visualizer = Rank1D(features=features, algorithm='shapiro')

visualizer.fit(X, y)                # Fit the data to the visualizer
visualizer.transform(X)             # Transform the data
visualizer.poof()


df = load_data("bikeshare")
feature = "weekday"
target = "workingday"

X = df[feature]
y = df[target]

from yellowbrick.features import JointPlotVisualizer

visualizer = JointPlotVisualizer(feature=feature, target=target)

visualizer.fit(X, y)
visualizer.poof()