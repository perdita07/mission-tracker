import pytest
from project import get_mission_by_name, get_missions_by_status, get_mission_achievements

# Test get_mission_by_name function
def test_get_mission_by_name():
    result = get_mission_by_name("Mangalyaan (Mars Orbiter Mission)")
    assert result is not None
    assert result["agency"] == "ISRO"
    assert result["status"] == "Completed"

    result = get_mission_by_name("Nonexistent Mission")
    assert result is None

# Test get_missions_by_status function
def test_get_missions_by_status():
    completed_missions = get_missions_by_status("Completed")
    assert len(completed_missions) > 0
    for mission in completed_missions.values():
        assert mission["status"] == "Completed"

    active_missions = get_missions_by_status("Active")
    assert len(active_missions) > 0
    for mission in active_missions.values():
        assert mission["status"] == "Active"

# Test get_mission_achievements function
def test_get_mission_achievements():
    achievements = get_mission_achievements("Mangalyaan (Mars Orbiter Mission)")
    assert len(achievements) > 0
    assert "First interplanetary mission by ISRO" in achievements

    achievements = get_mission_achievements("Nonexistent Mission")
    assert achievements == []

