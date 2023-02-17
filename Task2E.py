from floodsystem import stationdata
from floodsystem.plot import plot_water_levels
from floodsystem.flood import stations_highest_rel_level
import datetime, random
import matplotlib.pyplot as plt

stations = stationdata.build_station_list()
stationdata.update_water_levels(stations)
today = datetime.date.today()
start_date = datetime.date(today.year, today.month, today.day - 10)

for station in stations_highest_rel_level(stations, 5):
    plot_water_levels(station.measure_id, (start_date, today), station.typical_range)
