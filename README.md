# FunStrings

FunStrings is a comprehensive Python package that provides a wide range of functions for string manipulation, analysis, and transformation. It's designed to make working with strings easier and more efficient for developers, students, and educators.

## Features

FunStrings includes 24 utility functions organized into four categories:

### Basic String Operations
- **Reverse String:** Return the reversed string
- **Count Vowels:** Count the number of vowels in the string
- **Count Consonants:** Count the number of consonants
- **Check Palindrome:** Determine whether the string is a palindrome
- **To Upper/Lower:** Convert the string to uppercase or lowercase
- **Word Count:** Count the words in the string
- **Sort Characters:** Return the string with its characters sorted
- **Remove Whitespace:** Remove all whitespace from the string

### Text Analysis Functions
- **Word Frequencies:** Return frequency count of each word
- **Longest Word:** Find the longest word in the text
- **Shortest Word:** Find the shortest word in the text
- **Average Word Length:** Calculate average word length
- **Is Pangram:** Check if text contains all alphabet letters

### String Transformation Functions
- **Snake to Camel:** Convert snake_case to camelCase
- **Camel to Snake:** Convert camelCase to snake_case
- **Rotate String:** Rotate string by n positions
- **Shuffle String:** Randomly shuffle characters
- **Reverse Words:** Reverse order of words but not letters

### Pattern-based Functions
- **Extract Numbers:** Extract all numbers from text
- **Extract Emails:** Extract email addresses from text
- **Extract URLs:** Extract URLs from text
- **Mask Sensitive:** Mask all but last n chars with '*'
- **Find Repeated Words:** Find all repeated words in text

## Installation

You can install FunStrings directly from PyPI:

```bash
pip install funstrings
```

Or install from source:

```bash
pip install git+https://github.com/nilkanth02/funstrings.git
```

## Quick Start

```python
import funstrings

# Basic operations
text = "Hello, World!"
print(funstrings.reverse_string(text))  # !dlroW ,olleH
print(funstrings.count_vowels(text))    # 3

# Text analysis
sentence = "The quick brown fox jumps over the lazy dog"
print(funstrings.is_pangram(sentence))  # True
print(funstrings.longest_word(sentence))  # quick

# Transformations
snake = "hello_world_example"
print(funstrings.snake_to_camel(snake))  # helloWorldExample

# Pattern-based
text_with_emails = "Contact us at info@example.com or support@example.org"
print(funstrings.extract_emails(text_with_emails))  # ['info@example.com', 'support@example.org']
```

## Documentation

For detailed documentation and examples, visit the [GitHub repository](https://github.com/nilkanth02/funstrings).

## For Students and Educators

FunStrings is designed to be educational and beginner-friendly. It includes:

- Detailed docstrings with examples
- Comprehensive tutorials in the `tutorials/` directory
- Example scripts in the `examples/` directory
- Type hints for better IDE integration
