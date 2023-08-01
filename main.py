"""
main.py - Address Parser Controller

This script defines the AddressParserController class, which is responsible for parsing and splitting address strings
to extract relevant information such as street names and house numbers. It uses both regex and split-based parsing
methods for address extraction. The class inherits from the SplitParser, RegexParser, and ErrorLogger classes to
implement these parsing functionalities and handle errors gracefully.

Classes:
    AddressParserController - Controller class for parsing and splitting address strings.

Functions:
    get_split_by
    get_pattern
    __set_operation
    format_address
    operation

"""

from parser.regex_parser import RegexParser
from parser.split_parser import SplitParser
from utils.logger import ErrorLogger


class AddressParserController(SplitParser, RegexParser, ErrorLogger):
    def __init__(self, address: str):
        """
        Initialize the AddressParserController with the given address.

        Parameters:
            address (str): The address string to be parsed or split.

        Attributes:
            __OPERATION_TYPE (list): A list containing valid operation types: ["SPLIT", "PARSE"].
            __split_by (str): The string used for splitting the address (e.g., ",", "Flat", "House", etc.).
            __operation (str): The operation type ("SPLIT" or "PARSE") determined based on the address format.
            address (str): The input address to be processed.
            __pattern (str): The regex pattern used for address parsing.
            street_address (str): The extracted street name from the address.
            house_address (str): The extracted house number from the address.
        """
        super(AddressParserController, self).__init__()
        self.__OPERATION_TYPE: list = ["SPLIT", "PARSE"]
        self.__split_by: str = ""
        self.__operation: str = 'PARSE'
        self.address: str = address
        self.__pattern: str = r'\b(?:\d+(?:\s*[a-zA-Z]\b|\b)|No|Flat|Hous)\s*(?!\w)'
        self.street_address: str = ""
        self.house_address: str = ""
        self.__set_operation()

    def get_split_by(self) -> str:
        """
        Get the string used for splitting the address.

        Returns:
            str: The string used for splitting.
        """
        return self.__split_by

    def get_pattern(self) -> str:
        """
        Get the regex pattern used for address parsing.

        Returns:
            str: The regex pattern.
        """
        return self.__pattern

    def __set_operation(self) -> None:
        """
        Determine the appropriate operation type based on the address format.
        If a valid split keyword is found (e.g., "Flat", "House", etc.), the operation type is set to "SPLIT".
        Otherwise, the default operation type is "PARSE".
        """
        if "," in self.address.lower():
            self.__operation = 'SPLIT'
            self.__split_by = ","
        elif "flat" in self.address.lower():
            self.__operation = 'SPLIT'
            self.__split_by = "Flat"
        elif "house" in self.address.lower():
            self.__operation = 'SPLIT'
            self.__split_by = "House"
        elif "no" in self.address.lower():
            self.__operation = 'SPLIT'
            self.__split_by = "No"
        elif "building" in self.address.lower():
            self.__operation = 'SPLIT'
            self.__split_by = "Building"
        else:
            self.__operation = "PARSE"

    def format_address(self) -> dict:
        """
        Format the parsed address information into a dictionary.

        Returns:
            dict: A dictionary containing the extracted street and house information.
                Example: {"street": "Winterallee", "housenumber": "3"}
        """
        return {
            "street": self.street_address,
            "housenumber": self.house_address
        }

    def operation(self) -> dict:
        """
        Perform the appropriate parsing or splitting operation on the address.

        Returns:
            dict: A formatted dictionary containing the extracted street and house information.
        """
        try:
            if self.__operation not in self.__OPERATION_TYPE:
                return {"error": "Invalid Operation Type"}

            if self.__operation == "SPLIT" and self.__split_by == "":
                return {"error": "Invalid Operation Type"}

            if self.__operation == "SPLIT":
                return self.split_operation()
            else:
                return self.parse_operation()
        except Exception as e:
            self.log_error(e)


if __name__ == "__main__":

    test_addresses = [
        "Winterallee 3",
        "Musterstrasse 45",
        "Blaufeldweg 123B",
        "Am Bächle 23",
        "Auf der Vogelwiese 23 b",
        "4, rue de la revolution",
        "200 Broadway Av",
        "Calle Aduana, 29",
        "Calle 39 No 1540"
    ]

    for addr in test_addresses:
        result = AddressParserController(addr).operation()
        print(result)
