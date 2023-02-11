from .station import MonitoringStation

def stations_level_over_threshold(stations, tol):
    """Returns stations with water level above a given tolerance"""
    result = []
    for station in stations:
        rel = station.relative_water_level()
        if rel and rel > tol:
            result.append((station, rel))
    
    return result
