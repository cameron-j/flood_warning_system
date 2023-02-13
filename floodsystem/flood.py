def stations_level_over_threshold(stations, tol):
    """Returns stations with water level above a given tolerance"""
    result = []
    for station in stations:
        rel = station.relative_water_level()
        if rel and rel > tol:
            result.append((station, rel))
    
    return result

def stations_highest_rel_level(stations, N):
    has_data = list(filter(lambda s: s.relative_water_level() is not None, stations))
    return sorted(has_data, key=lambda s: s.relative_water_level(), reverse=True)[:N]
