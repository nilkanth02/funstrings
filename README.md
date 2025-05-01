# FunStrings

[![PyPI Version](https://img.shields.io/pypi/v/funstrings.svg)](https://pypi.org/project/funstrings/)
[![PyPI Downloads](https://static.pepy.tech/badge/funstrings/month)](https://pepy.tech/project/funstrings)
<!-- [![Python Versions](https://img.shields.io/pypi/pyversions/funstrings.svg)](https://pypi.org/project/funstrings/) -->
[![License](https://img.shields.io/pypi/l/funstrings.svg)](https://github.com/nilkanth02/funstrings/blob/main/LICENSE)
[![GitHub Stars](https://img.shields.io/github/stars/nilkanth02/funstrings.svg)](https://github.com/nilkanth02/funstrings/stargazers)
<!-- [![Code Style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black) -->
<!-- [![Total Downloads](https://static.pepy.tech/badge/funstrings)](https://pepy.tech/project/funstrings) -->
<!-- [![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/nilkanth02/funstrings/graphs/commit-activity) -->

FunStrings is a comprehensive Python package that provides a wide range of functions for string manipulation, analysis, and transformation. It's designed to make working with strings easier and more efficient for developers, students, and educators.

## Table of Contents

- [Features](#features)
  - [Basic String Operations](#basic-string-operations)
  - [Text Analysis Functions](#text-analysis-functions)
  - [String Transformation Functions](#string-transformation-functions)
  - [Pattern-based Functions](#pattern-based-functions)
  - [Data Cleaning Functions](#data-cleaning-functions)
  - [Text Analysis Helpers](#text-analysis-helpers)
  - [ML/NLP Preprocessing](#mlnlp-preprocessing)
  - [Validation Functions](#validation-functions)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Documentation](#documentation)
- [For Students and Educators](#for-students-and-educators)
- [Contributing](#contributing)
- [License](#license)
- [Connect](#connect)

## Features

FunStrings includes 44 utility functions organized into eight categories:

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

### Data Cleaning Functions
- **Remove HTML Tags:** Strip all HTML tags from text
- **Remove Emojis:** Remove emojis from text
- **Remove Special Characters:** Keep only letters and numbers
- **Expand Contractions:** Convert "don't" → "do not"
- **Correct Whitespace:** Remove weird spaces, tabs, newlines

### Text Analysis Helpers
- **Unique Words:** Return list of unique words
- **Most Common Word:** Return most frequent word
- **Sentence Count:** Number of sentences in text
- **Average Sentence Length:** Average words per sentence
- **Character Ratio:** Uppercase/lowercase/number ratio

### ML/NLP Preprocessing
- **Generate N-grams:** Generate list of n-grams
- **Strip Accents:** Remove accents (café → cafe)
- **Lemmatize Text:** Reduce words to base form
- **Is ASCII:** Check if text only contains ASCII

### Validation Functions
- **Is Valid Email:** Validate if a string is a proper email
- **Is Valid URL:** Validate if a string is a proper URL
- **Is Valid IP:** Check if string is a valid IP address
- **Is Valid Date:** Check if a string matches a date format
- **Contains Special Characters:** Check if special symbols are present

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

# Data cleaning
html_text = "<p>Hello <b>World</b></p>"
print(funstrings.remove_html_tags(html_text))  # Hello World
print(funstrings.expand_contractions("I don't know"))  # I do not know

# Text analysis helpers
print(funstrings.sentence_count("Hello! How are you? I'm fine."))  # 3
print(funstrings.most_common_word("hello world hello python"))  # hello

# ML/NLP preprocessing
print(funstrings.generate_ngrams("hello", 2))  # ['he', 'el', 'll', 'lo']
print(funstrings.strip_accents("café"))  # cafe

# Validation
print(funstrings.is_valid_email("user@example.com"))  # True
print(funstrings.is_valid_url("https://example.com"))  # True
```

## Documentation

For detailed documentation and examples, visit the [GitHub repository](https://github.com/nilkanth02/funstrings).

## For Students and Educators

FunStrings is designed to be educational and beginner-friendly. It includes:

- Detailed docstrings with examples
- Comprehensive tutorials in the `tutorials/` directory
- Example scripts in the `examples/` directory
- Type hints for better IDE integration

## Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Commit your changes: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature-name`
5. Submit a pull request

Please make sure to update tests as appropriate.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Connect

- GitHub: [nilkanth02](https://github.com/nilkanth02/)
- LinkedIn: [Nilkanth Ahire](https://www.linkedin.com/in/nilkanthahire)
