import plotly.plotly as py
from plotly.graph_objs import *
py.sign_in('kristian32', 'yKfcunxV5ywQ4S1omxf8')
f = open("data/co2.csv","r")
seznam = f.read().replace("\n",";").split(";")[3::3]
seznam_napisov =  []
sez = ["Alabama<br>", "Alaska<br>", "Arizona<br>", "Arkansas<br>", "California<br>", "Colorado<br>", "Connecticut<br>", "Delaware<br>", "Florida<br>Beef 42.6 Dairy 66.31<br>Fruits 1371.36 Veggies 450.86<br>Wheat 1.8 Corn 3.5", "Georgia<br>Beef 31.0 Dairy 38.38<br>Fruits 233.51 Veggies 154.77<br>Wheat 65.4 Corn 57.8", "Hawaii<br>Beef 4.0 Dairy 1.16<br>Fruits 55.51 Veggies 24.83<br>Wheat 0.0 Corn 0.0", "Idaho<br>Beef 119.8 Dairy 294.6<br>Fruits 21.64 Veggies 319.19<br>Wheat 568.2 Corn 24.0", "Illinois<br>Beef 53.7 Dairy 45.82<br>Fruits 12.53 Veggies 39.95<br>Wheat 223.8 Corn 2228.5", "Indiana<br>Beef 21.9 Dairy 89.7<br>Fruits 12.98 Veggies 37.89<br>Wheat 114.0 Corn 1123.2", "Iowa<br>Beef 289.8 Dairy 107.0<br>Fruits 3.24 Veggies 7.1<br>Wheat 3.1 Corn 2529.8", "Kansas<br>Beef 659.3 Dairy 65.45<br>Fruits 3.11 Veggies 9.32<br>Wheat 1426.5 Corn 457.3", "Kentucky<br>Beef 54.8 Dairy 28.27<br>Fruits 6.6 Veggies 0.0<br>Wheat 149.3 Corn 179.1", "Louisiana<br>Beef 19.8 Dairy 6.02<br>Fruits 17.83 Veggies 17.25<br>Wheat 78.7 Corn 91.4", "Maine<br>Beef 1.4 Dairy 16.18<br>Fruits 52.01 Veggies 62.9<br>Wheat 0.0 Corn 0.0", "Maryland<br>Beef 5.6 Dairy 24.81<br>Fruits 12.9 Veggies 20.43<br>Wheat 55.8 Corn 54.1", "Massachusetts<br>Beef 0.6 Dairy 5.81<br>Fruits 80.83 Veggies 21.13<br>Wheat 0.0 Corn 0.0", "Michigan<br>Beef 37.7 Dairy 214.82<br>Fruits 257.69 Veggies 189.96<br>Wheat 247.0 Corn 381.5", "Minnesota<br>Beef 112.3 Dairy 218.05<br>Fruits 7.91 Veggies 120.37<br>Wheat 538.1 Corn 1264.3", "Mississippi<br>Beef 12.8 Dairy 5.45<br>Fruits 17.04 Veggies 27.87<br>Wheat 102.2 Corn 110.0", "Missouri<br>Beef 137.2 Dairy 34.26<br>Fruits 13.18 Veggies 17.9<br>Wheat 161.7 Corn 428.8", "Montana<br>Beef 105.0 Dairy 6.82<br>Fruits 3.3 Veggies 45.27<br>Wheat 1198.1 Corn 5.4", "Nebraska<br>Beef 762.2 Dairy 30.07<br>Fruits 2.16 Veggies 53.5<br>Wheat 292.3 Corn 1735.9", "Nevada<br>Beef 21.8 Dairy 16.57<br>Fruits 1.19 Veggies 27.93<br>Wheat 5.4 Corn 0.0", "New Hampshire<br>Beef 0.6 Dairy 7.46<br>Fruits 7.98 Veggies 4.5<br>Wheat 0.0 Corn 0.0", "New Jersey<br>Beef 0.8 Dairy 3.37<br>Fruits 109.45 Veggies 56.54<br>Wheat 6.7 Corn 10.1", "New Mexico<br>Beef 117.2 Dairy 191.01<br>Fruits 101.9 Veggies 43.88<br>Wheat 13.9 Corn 11.2", "New York<br>Beef 22.2 Dairy 331.8<br>Fruits 202.56 Veggies 143.37<br>Wheat 29.9 Corn 106.1", "North Carolina<br>Beef 24.8 Dairy 24.9<br>Fruits 74.47 Veggies 150.45<br>Wheat 200.3 Corn 92.2", "North Dakota<br>Beef 78.5 Dairy 8.14<br>Fruits 0.25 Veggies 130.79<br>Wheat 1664.5 Corn 236.1", "Ohio<br>Beef 36.2 Dairy 134.57<br>Fruits 27.21 Veggies 53.53<br>Wheat 207.4 Corn 535.1", "Oklahoma<br>Beef 337.6 Dairy 24.35<br>Fruits 9.24 Veggies 8.9<br>Wheat 324.8 Corn 27.5", "Oregon<br>Beef 58.8 Dairy 63.66<br>Fruits 315.04 Veggies 126.5<br>Wheat 320.3 Corn 11.7", "Pennsylvania<br>Beef 50.9 Dairy 280.87<br>Fruits 89.48 Veggies 38.26<br>Wheat 41.0 Corn 112.1", "Rhode Island<br>Beef 0.1 Dairy 0.52<br>Fruits 2.83 Veggies 3.02<br>Wheat 0.0 Corn 0.0", "South Carolina<br>Beef 15.2 Dairy 7.62<br>Fruits 53.45 Veggies 42.66<br>Wheat 55.3 Corn 32.1", "South Dakota<br>Beef 193.5 Dairy 46.77<br>Fruits 0.8 Veggies 4.06<br>Wheat 704.5 Corn 643.6", "Tennessee<br>Beef 51.1 Dairy 21.18<br>Fruits 6.23 Veggies 24.67<br>Wheat 100.0 Corn 88.8", "Texas<br>Beef 961.0 Dairy 240.55<br>Fruits 99.9 Veggies 115.23<br>Wheat 309.7 Corn 167.2", "Utah<br>Beef 27.9 Dairy 48.6<br>Fruits 12.34 Veggies 6.6<br>Wheat 42.8 Corn 5.3", "Vermont<br>Beef 6.2 Dairy 65.98<br>Fruits 8.01 Veggies 4.05<br>Wheat 0.0 Corn 0.0", "Virginia<br>Beef 39.5 Dairy 47.85<br>Fruits 36.48 Veggies 27.25<br>Wheat 77.5 Corn 39.5", "Washington<br>Beef 59.2 Dairy 154.18<br>Fruits 1738.57 Veggies 363.79<br>Wheat 786.3 Corn 29.5", "West Virginia<br>Beef 12.0 Dairy 3.9<br>Fruits 11.54 Veggies 0.0<br>Wheat 1.6 Corn 3.5", "Wisconsin<br>Beef 107.3 Dairy 633.6<br>Fruits 133.8 Veggies 148.99<br>Wheat 96.7 Corn 460.5", "Wyoming<br>Beef 75.1 Dairy 2.89<br>Fruits 0.17 Veggies 10.23<br>Wheat 20.7 Corn 9.0"],
print(seznam)
for i in range(len(seznam_napisov)):
    seznam_napisov.append(sez[i]+" "+seznam[i])

trace1 = {
  "z": seznam,
  "autocolorscale": False,
  "colorbar": {"title": "yearBP"},
  "colorscale": [
    [0, "rgb(242,240,247)"], [0.2, "rgb(218,218,235)"], [0.4, "rgb(188,189,220)"], [0.6, "rgb(158,154,200)"], [0.8, "rgb(117,107,177)"], [1.0, "rgb(84,39,143)"]],
  "locationmode": "USA-states",
  "locations": ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"],
  "locationssrc": "kristian32:0:7af93d",
  "marker": {"line": {
      "color": "rgb(255,255,255)",
      "width": 2
    }},
  "name": "z",
  "text": seznam_napisov,
  "textsrc": "kristian32:0:01ba27",
  "type": "choropleth",
  "uid": "105dc6",
  "zauto": False,
  "zmax": 100,
  "zmin": -100,
  "zsrc": "kristian32:0:b28ef3"
}
data = Data([trace1])
layout = {
  "autosize": False,
  "geo": {
    "center": {
      "lat": 28.3626302944,
      "lon": -101.579079144
    },
    "lakecolor": "rgb(255, 255, 255)",
    "projection": {
      "scale": 0.613017430027,
      "type": "albers usa"
    },
    "scope": "world",
    "showlakes": True
  },
  "title": "US year bp"
}
fig = Figure(data=data, layout=layout)
plot_url = py.plot(fig)