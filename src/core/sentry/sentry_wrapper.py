import os
import sentry_sdk

from dotenv import load_dotenv

"""Generic wrapper class for implementing Sentry"""


class SentryWrapper:
    def __init__(self) -> None:
        load_dotenv()

        sentry_sdk.init(
            dsn=os.environ.get("SENTRY_DSN"),
            max_breadcrumbs=50,
            debug=False,
            enable_tracing=True,
            attach_stacktrace=True,
            traces_sample_rate=1.0,
            profiles_sample_rate=1.0,
            environment=os.getenv("ENVIRONMENT"),
        )

    def capture_exception(self, e: any) -> None:
        sentry_sdk.capture_exception(e)
        print(e)
