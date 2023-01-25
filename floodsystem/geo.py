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
