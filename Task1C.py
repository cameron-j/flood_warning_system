from floodsystem import geo, stationdata

stations = stationdata.build_station_list()

print(sorted(map(lambda s: s.name, geo.stations_within_radius(stations, (52.2053, 0.1218), 10))))
