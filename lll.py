import pandas as pd

with ZipFile(zip_file) as z:
  with z.open('AirQualityUCI.xlsx') as f:
    air_quality = pd.read_excel(
      f,
      index_col=0, parse_dates={'DateTime': [0, 1]}, #1
      na_values=[-200.0],                            #2
      convert_float=False                            #3
    )