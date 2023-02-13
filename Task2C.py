from floodsystem.flood import stations_highest_rel_level
from floodsystem import stationdata

stations = stationdata.build_station_list()
stationdata.update_water_levels(stations)

for station in stations_highest_rel_level(stations, 10):
    print(station.name, station.relative_water_level())
