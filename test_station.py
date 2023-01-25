# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the station module"""

from floodsystem.station import MonitoringStation
from floodsystem import station

test_stations = [
        MonitoringStation("TESTID1", "MEASUREID1", "LABEL1", (52.201720, 0.120078), (0, 1), "RIVER1", "TOWN1"),
        MonitoringStation("TESTID2", "MEASUREID2", "LABEL2", (54.484128, -1.804514), None, "RIVER2", "TOWN2"),
        MonitoringStation("TESTID3", "MEASUREID3", "LABEL3", (52.429970, -0.917557), (2, 1), "RIVER1", "TOWN3")
    ]

def test_create_monitoring_station():

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    assert s.station_id == s_id
    assert s.measure_id == m_id
    assert s.name == label
    assert s.coord == coord
    assert s.typical_range == trange
    assert s.river == river
    assert s.town == town

def test_typical_range_consistent():
    """Tests the typical_range_consistent method of the MonitoringStation"""
    assert not MonitoringStation("TESTID", "TESTMEASUREID", "TESTLABEL",
                                 (0, 1), None, "TESTRIVER", "TESTTOWN").typical_range_consistent()
    assert not MonitoringStation("TESTID", "TESTMEASUREID", "TESTLABEL",
                                 (0, 1), (2, 1), "TESTRIVER", "TESTTOWN").typical_range_consistent()
    assert MonitoringStation("TESTID", "TESTMEASUREID", "TESTLABEL",
                             (0, 1), (1, 2), "TESTRIVER", "TESTTOWN").typical_range_consistent()

def test_inconsistent_typical_range_stations():
    """Tests the inconsistent_typical_range_stations function"""
    assert station.inconsistent_typical_range_stations(test_stations) == test_stations[1:]
