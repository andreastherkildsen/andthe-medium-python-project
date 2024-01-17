from src.core.events.mock.mock_ecom import MockEcommerce


def test_mock_ecommerce_event() -> None:
    event_data = MockEcommerce.mock_ecommerce_event()

    assert "event" in event_data
    assert "product_id" in event_data
    assert "customer_id" in event_data
    assert "timestamp" in event_data
    assert isinstance(event_data["timestamp"], float)
