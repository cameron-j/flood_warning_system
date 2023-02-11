from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold
from pprint import pprint

stations = build_station_list()
update_water_levels(stations)

over_threshold = stations_level_over_threshold(stations, 0.8)
pprint([(station[0].name, station[1]) for station in over_threshold])

# for tol in range(100):
#     print(f"Tolerance = {tol * 0.01} : {len(stations_level_over_threshold(stations, tol * 0.01))} stations")
