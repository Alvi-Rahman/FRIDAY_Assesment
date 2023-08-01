"""
logger - Error Logger

This module provides the ErrorLogger class, which is responsible for logging errors encountered during address parsing.
The class sets up a basic configuration for the logging system and provides a method to log errors with timestamps.

Classes:
    ErrorLogger - Class for logging errors encountered during address parsing.

Functions:
    get_current_timestamp
    log_error

"""

import logging
import datetime


class ErrorLogger:
    def __init__(self):
        """
        Initialize the ErrorLogger and configure the logging system.

        The logging system is set up with the following settings:
            - The log messages are written to a file named 'error_logs.log'.
            - Only logs with ERROR level or above will be recorded.
            - The log message format includes the timestamp, log level, logger name, and message content.
        """
        logging.basicConfig(filename='error_logs.log', level=logging.ERROR,
                            format='%(asctime)s %(levelname)s %(name)s %(message)s')
        self.logger = logging.getLogger(__name__)

    @staticmethod
    def get_current_timestamp() -> str:
        """
        Get the current timestamp in the format 'YYYY-MM-DD HH:MM:SS'.

        Returns:
            str: The current timestamp as a string.
        """
        return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    def log_error(self, error: str) -> None:
        """
        Log an error message with a timestamp.

        Parameters:
            error (str): The error message to be logged.
        """
        self.logger.error(error)
