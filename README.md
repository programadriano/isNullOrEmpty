# is_null_or_empty Package

The `is_null_or_empty` package is a lightweight, versatile Python library designed to simplify and streamline the process of checking whether Python objects are `None` or empty. It supports a wide range of data types, including strings, lists, dictionaries, and more, making nullity and emptiness checks more efficient and readable.

## Key Features

- **Multi-Type Support**: Works seamlessly with strings, lists, dictionaries, and more.
- **Simplicity**: Provides a straightforward API that is easy to use in any project.
- **Efficiency**: Improves code readability by replacing multiple condition checks with a single, intuitive function call.

## Installation

Install `is_null_or_empty` quickly and easily using pip:

```bash
pip install is_null_or_empty
```

## Usage
The is_null_or_empty function can be used to check if an object is None or if it's an empty container (like a string, list, or dictionary). Here are some examples demonstrating its usage:

```bash
from is_null_or_empty import is_null_or_empty

print(is_null_or_empty(""))  # True
print(is_null_or_empty([]))  # True
print(is_null_or_empty({}))  # True
print(is_null_or_empty(None))  # True
print(is_null_or_empty("Some text"))  # False
print(is_null_or_empty([1, 2, 3]))  # False
```

As you can see, `is_null_or_empty` will return True for empty strings, lists, dictionaries, or None objects, and False otherwise, helping you make your code cleaner and more concise.

License
`is_null_or_empty` is licensed under the MIT License. Feel free to use it, modify it, and distribute it as you see fit.