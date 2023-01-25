from floodsystem import station
from floodsystem.stationdata import build_station_list

stations = build_station_list()

print(sorted(map(lambda s: s.name, station.inconsistent_typical_range_stations(stations))))
