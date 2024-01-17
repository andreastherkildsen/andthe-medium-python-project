from core.sentry.sentry_wrapper import SentryWrapper


def main() -> None:
    try:
        Exception("Manual exception made by ATHE")
    except Exception as e:
        SentryWrapper().capture_exception(e)


if __name__ == "__main__":
    main()
