import random
import time
from typing import Protocol


class PMockEcommerceEventData(Protocol):
    event: str
    product_id: int
    customer_id: str
    timestamp: float


"""Generic mock data event"""


class MockEcommerce:
    def mock_ecommerce_event() -> PMockEcommerceEventData:
        event_data = {
            "event": random.choice(
                [
                    "view_page",
                    "add_to_cart",
                    "checkout_started",
                    "order_completed",
                ],
            ),
            "product_id": random.choice([10100, 101001, 101002]),
            "customer_id": random.choice(
                [
                    "customer1@verdo.com",
                    "customer2@verdo.com",
                    "customer3@verdo.com",
                ],
            ),
            "timestamp": time.time(),
        }

        return event_data
