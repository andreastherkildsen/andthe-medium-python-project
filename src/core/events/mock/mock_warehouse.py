import random
import time
from typing import Protocol


class PWarehouseEventData(Protocol):
    event: str
    product_id: str
    location: str
    warehouse_id: str
    timestamp: float


"""Generic mock data event"""


class MockWarehouse:
    def mock_warehouse_event() -> PWarehouseEventData:
        event_data = {
            "event": random.choice(["add_to_stock", "remove_from_stock"]),
            "product_id": random.choice(["123", "456"]),
            "location": random.choice(["shelf_01", "shelf_02", "shelf_03"]),
            "warehouse_id": random.randint(1, 3),
            "timestamp": time.time(),
        }

        return event_data
