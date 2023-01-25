from floodsystem import geo, stationdata

stations = stationdata.build_station_list()

print(geo.rivers_by_station_number(stations, 9))
