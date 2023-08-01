# Address Parser (FRIDAY Assesment)

The Address Parser Project is a Python-based solution that parses and splits address strings to extract street names
and house numbers. The project consists of several modules and classes that work together to provide address parsing
and splitting functionalities.

## Table of Contents

- [Overview](#overview)
- [Modules and Classes](#modules-and-classes)
- [Usage](#usage)
- [Installation](#installation)
- [Testing](#testing)

## Overview

The Address Parser Project is designed to parse and split addresses in various formats. It uses both regex-based parsing
and split-based parsing methods to handle different address formats, ensuring accurate extraction of street and house
information.

The project is organized into the following main components:

- `main.py`: The main file containing the `AddressParserController` class that serves as the entry point for address parsing.
- `parser.regex_parser.py`: The module with the `RegexParser` class, responsible for parsing addresses using regular expressions.
- `parser.split_parser.py`: The module with the `SplitParser` class, responsible for splitting addresses based on specific keywords.
- `utils.logger.py`: The module with the `ErrorLogger` class, responsible for logging errors encountered during address parsing.
- `tests.test_controller.py`: The module with test cases for the `AddressParserController` class to ensure proper functionality.

## Modules and Classes

### AddressParserController

The `AddressParserController` class is the core controller responsible for parsing and splitting addresses. It utilizes
the `RegexParser` and `SplitParser` classes to perform the parsing operations. The class also logs any errors using the
`ErrorLogger` class.

### RegexParser

The `RegexParser` class provides the functionality to parse addresses using regular expressions. It extracts relevant
information such as street names and house numbers from the address.

### SplitParser

The `SplitParser` class is responsible for splitting addresses based on specific keywords or custom words. It uses string
splitting methods to extract street and house information from the address.

### ErrorLogger

The `ErrorLogger` class sets up a basic logging configuration to log errors encountered during address parsing. It writes
log messages to a file named 'error_logs.log' for future reference.

## Usage

To use the Address Parser Project, follow these steps:

1. Import the necessary classes from the modules into your Python script.
2. Create an instance of the `AddressParserController` class and pass the address to be parsed as an argument.
3. Call the `operation()` method of the `AddressParserController` class to parse or split the address.
4. The result will be a formatted dictionary containing the extracted street and house information.

Example:

```python
from main import AddressParserController

# Create an instance of AddressParserController with the address to be parsed
address = "Winterallee 3"
parser = AddressParserController(address)

# Call the operation() method to parse the address
result = parser.operation()
print(result)  # Output: {'street': 'Winterallee', 'housenumber': '3'}
```

## Installation
To install the Address Parser Project, follow these steps:

1. Clone the project repository to your local machine.
2. Install the required Python packages (if any) by running:

```shell
pip install -r requirements.txt
```
### The project is now ready to use.

## Testing

To run the test cases for the Address Parser Project, use the testing framework of your choice (e.g., Pytest):

```shell
pytest tests/test_controller.py
```

The test cases will ensure that the address parsing and splitting functionalities work as expected.

# Thank You!