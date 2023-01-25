from floodsystem import geo, stationdata

stations = stationdata.build_station_list()

print(sorted(geo.rivers_with_station(stations))[:10])

river_stations = geo.stations_by_river(stations)

def get_stations(river):
    """Returns a sorted list of stations on a given river"""
    return sorted(map(lambda s: s.name, river_stations[river]))

print(get_stations("River Aire"))
print(get_stations("River Cam"))
print(get_stations("River Thames"))
