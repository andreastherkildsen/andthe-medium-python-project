from src.core.events.mock.mock_warehouse import MockWarehouse


def test_mock_warehouse_event() -> None:
    event_data = MockWarehouse.mock_warehouse_event()

    assert "event" in event_data
    assert "product_id" in event_data
    assert "location" in event_data
    assert "warehouse_id" in event_data
    assert isinstance(event_data["timestamp"], float)
