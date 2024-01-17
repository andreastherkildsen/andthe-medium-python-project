from core.sentry.sentry_wrapper import SentryWrapper


def main() -> None:
    try:
        division_by_zero = 1 / 0
        print(division_by_zero)
    except Exception as e:
        SentryWrapper().capture_exception(e)


if __name__ == "__main__":
    main()
