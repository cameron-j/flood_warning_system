# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the station module"""

from floodsystem.station import MonitoringStation
from floodsystem import station
import pytest

test_stations = [
        MonitoringStation("TESTID1", "MEASUREID1", "LABEL1", (52.201720, 0.120078), (0, 1), "RIVER1", "TOWN1", "DATE1"),
        MonitoringStation("TESTID2", "MEASUREID2", "LABEL2", (54.484128, -1.804514), None, "RIVER2", "TOWN2", "DATE2"),
        MonitoringStation("TESTID3", "MEASUREID3", "LABEL3", (52.429970, -0.917557), (2, 1), "RIVER1", "TOWN3", "DATE3")
    ]

test_stations[0].latest_level = 0.2

def test_create_monitoring_station():

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    date = "some date"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town, date)

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
                                 (0, 1), None, "TESTRIVER", "TESTTOWN", "TESTDATE").typical_range_consistent()
    assert not MonitoringStation("TESTID", "TESTMEASUREID", "TESTLABEL",
                                 (0, 1), (2, 1), "TESTRIVER", "TESTTOWN", "TESTDATE").typical_range_consistent()
    assert MonitoringStation("TESTID", "TESTMEASUREID", "TESTLABEL",
                             (0, 1), (1, 2), "TESTRIVER", "TESTTOWN", "TESTDATE").typical_range_consistent()

def test_inconsistent_typical_range_stations():
    """Tests the inconsistent_typical_range_stations function"""
    assert station.inconsistent_typical_range_stations(test_stations) == test_stations[1:]

def test_private_attributes():
    """Tests that the attributes of the MonitoringStation class cannot be changed dynamically"""
    s = test_stations[0]
    with pytest.raises(AttributeError):
        s.station_id = "NEWID"
    with pytest.raises(AttributeError):
        s.measure_id = "NEWMEASUREID"
    with pytest.raises(AttributeError):
        s.name = "NEWLABEL"
    with pytest.raises(AttributeError):
        s.coord = (7, 8)
    with pytest.raises(AttributeError):
        s.typical_range = (9, 10)
    with pytest.raises(AttributeError):
        s.river = "NEWRIVER"
    with pytest.raises(AttributeError):
        s.town = "NEWTOWN"
    with pytest.raises(AttributeError):
        s.date_opened = "NEWDATE"

def test_relative_water_level():
    """Tests the calculation of relative water level"""
    assert test_stations[0].relative_water_level() == 0.2
    assert test_stations[1].relative_water_level() is None
    assert test_stations[2].relative_water_level() is None
