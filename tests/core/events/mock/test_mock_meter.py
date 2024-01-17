from src.core.events.mock.mock_meter import MockMeter


def test_mock_meter_event() -> None:
    event_data = MockMeter.mock_meter_event()

    assert "event" in event_data
    assert "customer_email" in event_data
    assert "location" in event_data
    assert "kwh" in event_data
    assert isinstance(event_data["timestamp"], float)
