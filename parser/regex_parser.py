"""
regex_parser - Regular Expression Parser

This module provides the RegexParser class, which is responsible for parsing an address string using regular expressions.
The class utilizes the `re` module to extract relevant information such as street names and house numbers from the address.

Classes:
    RegexParser - Class for parsing address strings using regular expressions.

Functions:
    parse_address_using_regex
    parse_operation

"""

import re


class RegexParser:
    def parse_address_using_regex(self) -> dict:
        """
        Parse the address using regular expressions to extract street and house information.

        Returns:
            dict: A formatted dictionary containing the extracted street and house information.
                Example: {"street": "Winterallee", "housenumber": "3"}
        """
        if self.address is None or self.address == "" or type(self.address) != str:
            return {"error": "Invalid Address Given"}

        self.house_address = re.findall(self.get_pattern(), self.address)[0]
        self.street_address = self.address.replace(self.house_address, "").strip().replace(",", "")
        return self.format_address()

    def parse_operation(self) -> dict:
        """
        Perform address parsing using regular expressions.

        Returns:
            dict: A formatted dictionary containing the extracted street and house information.
        """
        return self.parse_address_using_regex()
