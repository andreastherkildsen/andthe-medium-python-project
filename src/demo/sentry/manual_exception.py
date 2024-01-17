from core.sentry.sentry_wrapper import SentryWrapper


def main() -> None:
    try:
        Exception("Generic Exception thrown by python script")
    except Exception as e:
        SentryWrapper().capture_exception(e)


if __name__ == "__main__":
    main()
