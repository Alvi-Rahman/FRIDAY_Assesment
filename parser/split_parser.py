"""
split_parser - Split-based Parser

This module provides the SplitParser class, which is responsible for splitting an address string based on specific
keywords such as "," or custom words like "Flat," "House," etc. The class uses string splitting methods to extract
relevant information such as street names and house numbers from the address.

Classes:
    SplitParser - Class for splitting address strings based on specific keywords or custom words.

Functions:
    find_next_word
    comma_split_operation
    word_split_operation
    split_operation

"""

import re


class SplitParser:
    def find_next_word(self, word: str) -> str:
        """
        Find the next word following a given word in the address.

        Parameters:
            word (str): The word to find in the address.

        Returns:
            str: The next word after the given word, if found; otherwise, returns None.
        """
        pattern = r'(?<=\b' + re.escape(word) + r'\b)\s+(\w+)'
        match = re.search(pattern, self.address, re.IGNORECASE)
        if match:
            return match.group(1)
        else:
            return None

    def comma_split_operation(self) -> dict:
        """
        Split the address using a comma separator and extract street and house information.

        Returns:
            dict: A formatted dictionary containing the extracted street and house information.
                Example: {"street": "Winterallee", "housenumber": "3"}
        """
        address_1, address_2 = self.address.split(self.get_split_by())
        address_1, address_2 = address_1.strip(), address_2.strip()
        if address_1[0].isdigit():
            self.house_address = address_1
            self.street_address = address_2
        elif address_2[0].isdigit():
            self.house_address = address_2
            self.street_address = address_1
        else:
            return self.parse_operation()

        return self.format_address()

    def word_split_operation(self) -> dict:
        """
        Split the address using a custom word separator and extract street and house information.

        Returns:
            dict: A formatted dictionary containing the extracted street and house information.
                Example: {"street": "Winterallee", "housenumber": "3"}
        """
        house_no = self.find_next_word(self.get_split_by())
        if house_no is None:
            return self.parse_operation()
        else:
            self.house_address = f"{self.get_split_by()} {house_no}"
            self.street_address = self.address.replace(self.house_address, "").replace(",", "") \
                .replace(self.house_address.lower(), "").strip()

        return self.format_address()

    def split_operation(self) -> dict:
        """
        Perform address splitting based on the specified separator.

        Returns:
            dict: A formatted dictionary containing the extracted street and house information.
        """
        if self.get_split_by() == ",":
            return self.comma_split_operation()
        else:
            return self.word_split_operation()
