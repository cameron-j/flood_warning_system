from floodsystem import geo, stationdata
from pprint import pprint

stations = geo.stations_by_distance(stationdata.build_station_list(), (52.2053, 0.1218))

print("\n\n[ CLOSEST 10 STATIONS ]")
pprint(stations[:10])
print("\n\n[ FURTHEST 10 STATIONS ]")
pprint(stations[-10:])