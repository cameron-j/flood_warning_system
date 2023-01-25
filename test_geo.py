from floodsystem import geo
from floodsystem.station import MonitoringStation

def test_stations_by_distance():
    """Test the geo.stations_by_distance() function"""
    stations = [
        MonitoringStation("TESTID1", "MEASUREID1", "LABEL1", (2, 3), (0, 1), "RIVER1", "TOWN1"),
        MonitoringStation("TESTID2", "MEASUREID2", "LABEL2", (0, 4), (0, 1), "RIVER2", "TOWN2"),
        MonitoringStation("TESTID3", "MEASUREID3", "LABEL3", (2, 3), (0, 1), "RIVER3", "TOWN3")
    ]
    res = geo.stations_by_distance(stations, (5, 1))
    assert res[0].station_id == "TESTID1"
    assert res[1].station_id == "TESTID3"
    assert res[2].station_id == "TESTID2"
