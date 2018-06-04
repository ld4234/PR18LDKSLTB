import matplotlib.pyplot as plt
from csv import DictReader

reader = DictReader(open('data/GlobalTemperatures.csv', 'rt', encoding='utf-8'))
temp = []
for row in reader:
    if(int(row["dt"][:4]) > 1957):
        try:
            temp.append(float(row["LandAverageTemperature"]))
        except:
            temp.append(temp[-1])

reader = DictReader(open('data/co2_by_year.csv', 'rt', encoding='utf-8'))
co2 = []
for row in reader:
    if(int(row["Year"]) < 2016):
        try:
            co2.append(float(row["Carbon Dioxide (ppm)"]))
        except:
            try:
                co2.append(co2[-1])
            except:
                co2.append(315)

plt.figure()
plt.plot(temp, co2, 'r')
axes = plt.gca()
axes.set_xlim([min(temp),max(temp)])
axes.set_ylim([min(co2),max(co2)])
plt.xlabel('Povprecna temperatura')
plt.ylabel('Vrednost co2 ppm');
plt.title("Odvisnost med temperaturo in co2")
plt.show()




"""
reader = (open('data/GlobalTemperatures.csv', 'rt', encoding='utf-8'))
temp = []
for row in reader:
    if(row[:2] != "dt" and int(row.split(",")[0][:4]) > 1957):
        try:
            temp.append(float(row.split(",")[1]))
        except:
            temp.append(temp[-1])

reader = (open('data/co2_by_year.csv', 'rt', encoding='utf-8'))
co2 = []
for row in reader:
    if(row[:1] != "Y" and int(row.split(",")[0]) < 2016):
        try:
            co2.append(float(row.split(",")[3]))
        except:
            try:
                co2.append(co2[-1])
            except:
                co2.append(315)
"""