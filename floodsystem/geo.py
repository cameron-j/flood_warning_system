# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

# haversine(a, b) returns the distance from a to b in km
from haversine import haversine

def stations_by_distance(stations, p):
    """Sorts the stations by distance from p"""
    return sorted(stations, key=lambda s: haversine(p, s.coord))

def stations_within_radius(stations, centre, r):
    """Returns a list of monitoring stations within a radius r (km) of centre"""
    in_radius = []
    for station in stations:
        if haversine(centre, station.coord) <= r:
            in_radius.append(station)
    
    return in_radius

def rivers_with_station(stations):
    """Returns a list of rivers with a monitoring station"""
    return set(station.river for station in stations)

def stations_by_river(stations):
    """Returns a dictionary mapping river names to stations on the river"""
    river_stations = {}
    for station in stations:
        try:
            river_stations[station.river].append(station)
        except KeyError:
            river_stations[station.river] = [station]
    
    return river_stations

def rivers_by_station_number(stations, N):
    """Returns the N rivers with the greatest number of stations sorted by number of stations"""
    river_stations = stations_by_river(stations)

    river_counts = []
    for river in river_stations.keys():
        river_counts.append((river, len(river_stations[river])))
    
    return sorted(river_counts, key=lambda x: x[1], reverse=True)[:N]
