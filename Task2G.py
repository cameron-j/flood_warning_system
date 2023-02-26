from floodsystem import stationdata, datafetcher, analysis
import datetime
from scipy.optimize import curve_fit
from matplotlib.dates import date2num, num2date
import numpy as np

stations = stationdata.build_station_list()
stationdata.update_water_levels(stations)

severities = {
    "Severe": [],
    "High": [],
    "Moderate": [],
    "Low": []
}
for station in stations:
    latest = station.latest_level
    if not station.latest_level:
        continue
    
    if latest > 0.5:
        if latest > 1:
            if latest > 2:
                severities["Severe"].append(station)
            else:
                severities["High"].append(station)
        else:
            severities["Moderate"].append(station)
    else:
        severities["Low"].append(station)

for severity in severities.keys():
    print(severity + ": \n\t")
    for station in severities[severity]:
        print(station.name + ", ", end="")
    print("\n\n")
