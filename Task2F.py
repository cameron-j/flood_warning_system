from floodsystem.plot import plot_water_level_with_fit
from floodsystem import stationdata
from floodsystem.flood import stations_highest_rel_level
from floodsystem.datafetcher import fetch_measure_levels
import datetime

stations = stationdata.build_station_list()
stationdata.update_water_levels(stations)
today = datetime.date.today()
dt = datetime.timedelta(days=2)

for station in stations_highest_rel_level(stations, 5):
    dates, levels = fetch_measure_levels(station.measure_id, dt=dt)
    plot_water_level_with_fit(station, dates, levels, 4)
