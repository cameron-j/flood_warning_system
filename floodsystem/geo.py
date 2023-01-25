# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from haversine import haversine

def stations_by_distance(stations, p):
    """Sorts the stations by distance from p"""
    return sorted(stations, key=lambda s: haversine(p, s.coord))
