# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module provides a model for a monitoring station, and tools
for manipulating/modifying station data

"""


class MonitoringStation:
    """This class represents a river level monitoring station"""

    def __init__(self, station_id, measure_id, label, coord, typical_range,
                 river, town, date_opened):

        self._station_id = station_id
        self._measure_id = measure_id

        # Handle case of erroneous data where data system returns
        # '[label, label]' rather than 'label'
        self._name = label
        if isinstance(label, list):
            self._name = label[0]

        self._coord = coord
        self._typical_range = typical_range
        self._river = river
        self._town = town
        self._date_opened = date_opened

        self.latest_level = None
    
    @property
    def station_id(self):
        return self._station_id
    
    @property
    def measure_id(self):
        return self._measure_id
    
    @property
    def name(self):
        return self._name
    
    @property
    def coord(self):
        return self._coord
    
    @property
    def typical_range(self):
        return self._typical_range
    
    @property
    def river(self):
        return self._river
    
    @property
    def town(self):
        return self._town
    
    @property
    def date_opened(self):
        return self._date_opened

    def __repr__(self):
        d = "Station name:     {}\n".format(self.name)
        d += "   id:            {}\n".format(self.station_id)
        d += "   date opened:   {}\n".format(self.date_opened)
        d += "   measure id:    {}\n".format(self.measure_id)
        d += "   coordinate:    {}\n".format(self.coord)
        d += "   town:          {}\n".format(self.town)
        d += "   river:         {}\n".format(self.river)
        d += "   typical range: {}".format(self.typical_range)
        return d
    
    def typical_range_consistent(self):
        """Checks if the typical range of a station is consistent (exists and lower value comes first)"""
        return self.typical_range!=None and self.typical_range[0] <= self.typical_range[1]

def inconsistent_typical_range_stations(stations):
    """Returns a list of stations with inconsistent typical ranges"""
    return list(filter(lambda s: not s.typical_range_consistent(), stations))
