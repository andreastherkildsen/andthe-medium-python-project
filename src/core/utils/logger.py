import datetime
import os


"""Generic utility class for writing logs to directory"""


class Logger:
    logs_dir = "logs/"
    default_log = "default.log"

    """Log method, provide message and optional path"""

    def log(message: str, file_name=None) -> True:
        try:
            if not file_name:
                file_name = Logger.default_log

            # Create the directory if it doesn't exist
            if not os.path.exists(Logger.logs_dir):
                os.makedirs(Logger.logs_dir)

            with open(os.path.join(Logger.logs_dir, file_name), "a") as file:
                file.write(str(datetime.datetime.now()) + " : " + str(message) + "\n")

            return True
        except Exception as e:
            print("Could not write to log", e)
            raise e
