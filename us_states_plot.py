import plotly.plotly as py
from plotly.graph_objs import *
py.sign_in('kristian32', 'yKfcunxV5ywQ4S1omxf8')
f = open("data/temp_us_states.csv","r")
seznam = f.read().replace("\n","\t").split("\t")[2::4]
seznam_napisov =  []
sez = ["Alabama<br>", "Alaska<br>", "Arizona<br>", "Arkansas<br>", "California<br>", "Colorado<br>", "Connecticut<br>", "Delaware<br>", "Florida<br>", "Georgia<br>", "Hawaii<br>", "Idaho<br>", "Illinois<br>", "Indiana<br>", "Iowa<br>", "Kansas<br>", "Kentucky<br>", "Louisiana<br>", "Maine<br>", "Maryland<br>", "Massachusetts<br>", "Michigan<br>", "Minnesota<br>", "Mississippi<br>", "Missouri<br>", "Montana<br>", "Nebraska<br>", "Nevada<br>", "New Hampshire<br>", "New Jersey<br>", "New Mexico<br>", "New York<br>", "North Carolina<br>", "North Dakota<br>", "Ohio<br>", "Oklahoma<br>", "Oregon<br>", "Pennsylvania<br>", "Rhode Island<br>", "South Carolina<br>", "South Dakota<br>", "Tennessee<br>", "Texas<br>", "Utah<br>", "Vermont<br>", "Virginia<br>", "Washington<br>", "West Virginia<br>", "Wisconsin<br>", "Wyoming<br>"]

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
  "zmax": 20,
  "zmin": -5,
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
  "title": "US temperatures 2018"
}
fig = Figure(data=data, layout=layout)
plot_url = py.plot(fig)