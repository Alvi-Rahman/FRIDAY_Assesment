"""
tests.test_controller - Test Cases for Address Parser Controller

This module contains test cases for the AddressParserController class. The test cases cover both successful parsing and
splitting operations and scenarios where an invalid address is provided.

Classes:
    TestAddressParserController - Test class for AddressParserController.

Functions:
    test_parse_operation_success
    test_split_operation_success
    test_parse_address_invalid

"""

from main import AddressParserController


class TestAddressParserController:
    def test_parse_operation_success(self):
        """
        Test successful parsing operations.

        Run test cases where the AddressParserController successfully parses the address and returns the expected
        result containing the street and house information.

        Returns:
            None
        """
        test_cases = [
            ("Winterallee 3", {"street": "Winterallee", "housenumber": "3"}),
            ("Musterstrasse 45", {"street": "Musterstrasse", "housenumber": "45"}),
            ("Blaufeldweg 123B", {"street": "Blaufeldweg", "housenumber": "123B"}),
            ("Am Bächle 23", {"street": "Am Bächle", "housenumber": "23"}),
            ("Auf der Vogelwiese 23 b", {"street": "Auf der Vogelwiese", "housenumber": "23 b"}),
            ("4, rue de la revolution", {"street": "rue de la revolution", "housenumber": "4"}),
            ("200 Broadway Av", {"street": "Broadway Av", "housenumber": "200"}),
            ("Calle Aduana, 29", {"street": "Calle Aduana", "housenumber": "29"}),
            ("Calle 39 No 1540", {"street": "Calle 39", "housenumber": "No 1540"})
        ]

        for address, expected_result in test_cases:
            parser = AddressParserController(address)
            assert parser.operation() == expected_result

    def test_split_operation_success(self):
        """
        Test successful splitting operations.

        Run test cases where the AddressParserController successfully splits the address and returns the expected
        result containing the street and house information.

        Returns:
            None
        """
        test_cases = [
            ("Winterallee flat 3", {"street": "Winterallee", "housenumber": "Flat 3"}),
            ("Musterstrasse house 45", {"street": "Musterstrasse", "housenumber": "House 45"}),
            ("Blaufeldweg, 123B", {"street": "Blaufeldweg", "housenumber": "123B"}),
            ("Auf der Vogelwiese Flat 23", {"street": "Auf der Vogelwiese", "housenumber": "Flat 23"}),
            ("Calle Aduana, 29", {"street": "Calle Aduana", "housenumber": "29"})
        ]

        for address, expected_result in test_cases:
            parser = AddressParserController(address)
            assert parser.operation() == expected_result

    def test_parse_address_invalid(self):
        """
        Test invalid address parsing.

        Run test cases where the AddressParserController receives an invalid address and returns the expected
        error message.

        Returns:
            None
        """
        test_cases = [
            ("", 'Invalid Address Given'),
        ]

        for address, expected_result in test_cases:
            parser = AddressParserController(address)
            assert parser.operation() == expected_result
