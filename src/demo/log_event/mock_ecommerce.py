from core.events.mock.mock_ecom import MockEcommerce
from core.utils.logger import Logger
from core.sentry.sentry_wrapper import SentryWrapper


def main() -> None:
    try:
        event = MockEcommerce.mock_ecommerce_event()
        Logger.log(event, "ecommerce-event.log")
        print("Ecommerce event {event} has been mocked and logged")
    except Exception as e:
        SentryWrapper().capture_exception(e)


if __name__ == "__main__":
    main()
