from floodsystem import flood
from floodsystem.station import MonitoringStation
import pytest

test_stations = [
        MonitoringStation("TESTID1", "MEASUREID1", "LABEL1", (52.201720, 0.120078), (0, 1), "RIVER1", "TOWN1", "DATE1"),
        MonitoringStation("TESTID2", "MEASUREID2", "LABEL2", (54.484128, -1.804514), (0, 3), "RIVER2", "TOWN2", "DATE2"),
        MonitoringStation("TESTID3", "MEASUREID3", "LABEL3", (52.429970, -0.917557), (2, 5), "RIVER1", "TOWN3", "DATE3")
    ]

def test_stations_level_over_threshold():
    """Tests the stations_level_over_threshold() function"""
    test_stations[0].latest_level = 0.9
    test_stations[1].latest_level = 2.1
    test_stations[2].latest_level = 3.5
    print(flood.stations_level_over_threshold(test_stations, 0.6))
    assert flood.stations_level_over_threshold(test_stations, 0.6) == [(test_stations[0], pytest.approx(0.9)), (test_stations[1], pytest.approx(0.7))]