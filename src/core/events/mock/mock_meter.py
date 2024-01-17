import random
import time
from typing import Protocol


class PMockMeterEventData(Protocol):
    event: str
    customer_email: str
    location: str
    kwh: int
    timestamp: float


"""Generic mock data event"""


class MockMeter:
    def mock_meter_event() -> PMockMeterEventData:
        event_data = {
            "event": "installtion_comsumption_eletrical_panel",
            "customer_email": random.choice(
                [
                    "customer1@verdo.com",
                    "customer2@verdo.com",
                    "customer3@verdo.com",
                ],
            ),
            "location": random.choice(["Randers", "Herning", "Næstved"]),
            "kwh": random.randint(50, 300),
            "timestamp": time.time(),
        }

        return event_data
