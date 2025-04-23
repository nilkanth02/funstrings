#!/usr/bin/env python
"""
Basic Usage Example for FunStrings Package

This script demonstrates the basic functionality of the FunStrings package.
It's designed to be educational and easy to understand for beginners.

For students:
- This example shows how to import and use functions from a package
- Each function is demonstrated with clear examples
- The output is formatted to be easy to read and understand
"""

import funstrings

def main():
    """Demonstrate the basic functionality of the FunStrings package."""

    # Example string to work with
    example = "Hello, World! This is a test string."

    print("=" * 60)
    print("FunStrings Package - Basic Usage Example")
    print("=" * 60)
    print(f"Original string: '{example}'")
    print("-" * 60)

    # Demonstrate string reversal
    print(f"Reversed:        '{funstrings.reverse_string(example)}'")

    # Demonstrate case conversion
    print(f"Uppercase:       '{funstrings.to_upper(example)}'")
    print(f"Lowercase:       '{funstrings.to_lower(example)}'")

    # Demonstrate counting functions
    print(f"Vowel count:     {funstrings.count_vowels(example)}")
    print(f"Consonant count: {funstrings.count_consonants(example)}")
    print(f"Word count:      {funstrings.word_count(example)}")

    # Demonstrate character sorting
    print(f"Sorted chars:    '{funstrings.sort_characters(example)}'")
    print(f"Sorted (desc):   '{funstrings.sort_characters(example, reverse=True)}'")

    # Demonstrate whitespace removal
    print(f"No whitespace:   '{funstrings.remove_whitespace(example)}'")

    # Demonstrate palindrome checking
    print(f"Is palindrome:   {funstrings.is_palindrome(example)}")

    # Try with a palindrome
    palindrome = "A man, a plan, a canal: Panama"
    print("-" * 60)
    print(f"New string:      '{palindrome}'")
    print(f"Is palindrome:   {funstrings.is_palindrome(palindrome)}")

    print("=" * 60)
    print("End of example")
    print("=" * 60)

if __name__ == "__main__":
    main()
