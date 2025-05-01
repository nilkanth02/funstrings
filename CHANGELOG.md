# Changelog

All notable changes to the FunStrings package will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.2] - 2024-05-01

### Added
- Connect section in README with GitHub and LinkedIn links
- Added 5 Data Cleaning Functions:
  - `remove_html_tags`: Strip all HTML tags from text
  - `remove_emojis`: Remove emojis from text
  - `remove_special_characters`: Keep only letters and numbers
  - `expand_contractions`: Convert contractions like "don't" to "do not"
  - `correct_whitespace`: Remove weird spaces, tabs, newlines

- Added 5 Text Analysis Helpers:
  - `unique_words`: Return list of unique words
  - `most_common_word`: Return most frequent word
  - `sentence_count`: Number of sentences in text
  - `average_sentence_length`: Average words per sentence
  - `character_ratio`: Uppercase/lowercase/number ratio

- Added 4 ML/NLP Preprocessing Functions:
  - `generate_ngrams`: Generate list of n-grams
  - `strip_accents`: Remove accents (café → cafe)
  - `lemmatize_text`: Reduce words to base form
  - `is_ascii`: Check if text only contains ASCII

- Added 5 Validation Functions:
  - `is_valid_email`: Validate if a string is a proper email
  - `is_valid_url`: Validate if a string is a proper URL
  - `is_valid_ip`: Check if string is a valid IP address
  - `is_valid_date`: Check if a string matches a date format
  - `contains_special_characters`: Check if special symbols are present

### Documentation
- Updated README.md with new function categories
- Added examples for all new functions
- Created new example file: v0.1.1_functions_demo.py
- Added comprehensive test suite for new functions

## [0.1.1] - 2024-04-23

### Added
- Added badges to README.md (PyPI version, downloads, Python versions, license, etc.)
- Added Table of Contents to README.md for better navigation
- Added Contributing section to README.md
- Added License section to README.md
- Created CHANGELOG.md file to track changes

### Changed
- Renamed package from "stringfun" to "funstrings"
- Updated all import statements and references in documentation
- Improved README.md with more detailed information

## [0.1.0] - 2024-04-22

### Added
- Initial release of the package
- Basic string operations (reverse, count vowels/consonants, palindrome check, etc.)
- Text analysis functions (word frequencies, longest/shortest word, etc.)
- String transformation functions (snake_to_camel, camel_to_snake, rotate, shuffle, etc.)
- Pattern-based functions (extract numbers/emails/URLs, mask sensitive data, etc.)
- Comprehensive documentation and examples
- Educational tutorials for beginners and students
