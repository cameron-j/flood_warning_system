from floodsystem import geo
from floodsystem.station import MonitoringStation

test_stations = [
        MonitoringStation("TESTID1", "MEASUREID1", "LABEL1", (52.201720, 0.120078), (0, 1), "RIVER1", "TOWN1"),
        MonitoringStation("TESTID2", "MEASUREID2", "LABEL2", (54.484128, -1.804514), (0, 1), "RIVER2", "TOWN2"),
        MonitoringStation("TESTID3", "MEASUREID3", "LABEL3", (52.429970, -0.917557), (0, 1), "RIVER1", "TOWN3")
    ]

def test_stations_by_distance():
    """Test the geo.stations_by_distance() function"""
    res = geo.stations_by_distance(test_stations, (52.319076, -0.061522))
    assert res[0].station_id == "TESTID1"
    assert res[1].station_id == "TESTID3"
    assert res[2].station_id == "TESTID2"

def test_stations_within_radius():
    """Test the geo.stations_within_radius function"""
    res = geo.stations_within_radius(test_stations, (52.319076, -0.061522), 100)
    assert len(res) == 2
    assert res[0].station_id == "TESTID1"
    assert res[1].station_id == "TESTID3"

def test_rivers_with_station():
    """Test the geo.rivers_within_radius function"""
    res = geo.rivers_with_station(test_stations)
    assert res == set(("RIVER1", "RIVER2"))

def test_stations_by_river():
    """Test the geo.stations_by_river function"""
    res = geo.stations_by_river(test_stations)
    assert res == {
        "RIVER1" : [test_stations[0], test_stations[2]],
        "RIVER2" : [test_stations[1]]
    }

def test_rivers_by_station_number():
    """Test the geo.rivers_by_station_number function"""
    assert geo.rivers_by_station_number(test_stations, 2) == [("RIVER1", 2), ("RIVER2", 1)]
    assert geo.rivers_by_station_number(test_stations, 1) == [("RIVER1", 2)]
