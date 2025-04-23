#!/usr/bin/env python
"""
String Manipulation Basics Tutorial

This tutorial demonstrates the basic concepts of string manipulation in Python
using the FunStrings package. It's designed for beginners and students who are
learning Python programming.

Learning Objectives:
1. Understand what strings are in Python
2. Learn basic string operations
3. See how to use the FunStrings package for common string tasks
4. Practice with examples and exercises

To run this tutorial:
1. Install the FunStrings package: pip install funstrings
2. Run this script: python string_manipulation_basics.py
"""

import funstrings

def print_section(title):
    """Helper function to print a section title."""
    print("\n" + "=" * 70)
    print(f" {title} ".center(70, "="))
    print("=" * 70)

def introduction():
    """Introduction to strings in Python."""
    print_section("INTRODUCTION TO STRINGS")

    print("In Python, strings are sequences of characters enclosed in quotes.")
    print("They can be defined using single quotes ('), double quotes (\"), or triple quotes (''' or \"\"\").")

    print("\nExamples:")
    print("  'Hello, World!'                  # Single quotes")
    print("  \"Python Programming\"             # Double quotes")
    print("  '''This is a multi-line string''' # Triple quotes")

    print("\nStrings are immutable, which means once created, their content cannot be changed.")
    print("Any operation that appears to modify a string actually creates a new string.")

def basic_operations():
    """Demonstrate basic string operations."""
    print_section("BASIC STRING OPERATIONS")

    example = "Hello, Python!"

    print(f"Working with the string: '{example}'")
    print("\n1. String Length")
    print(f"   len('{example}') = {len(example)}")

    print("\n2. Accessing Characters (Indexing)")
    print(f"   '{example}'[0] = '{example[0]}'  # First character")
    print(f"   '{example}'[7] = '{example[7]}'  # 8th character")
    print(f"   '{example}'[-1] = '{example[-1]}'  # Last character")

    print("\n3. Slicing")
    print(f"   '{example}'[0:5] = '{example[0:5]}'  # Characters from index 0 to 4")
    print(f"   '{example}'[7:] = '{example[7:]}'  # Characters from index 7 to the end")
    print(f"   '{example}'[:5] = '{example[:5]}'  # Characters from the beginning to index 4")

    print("\n4. Concatenation")
    print(f"   'Hello, ' + 'Python!' = '{'Hello, ' + 'Python!'}'")

    print("\n5. Repetition")
    print(f"   'Python! ' * 3 = '{'Python! ' * 3}'")

def using_stringfun():
    """Demonstrate using the FunStrings package."""
    print_section("USING THE FUNSTRINGS PACKAGE")

    example = "Hello, Python Programming!"

    print(f"Working with the string: '{example}'")

    print("\n1. Case Conversion")
    print(f"   funstrings.to_upper('{example}') = '{funstrings.to_upper(example)}'")
    print(f"   funstrings.to_lower('{example}') = '{funstrings.to_lower(example)}'")

    print("\n2. Counting")
    print(f"   funstrings.count_vowels('{example}') = {funstrings.count_vowels(example)}")
    print(f"   funstrings.count_consonants('{example}') = {funstrings.count_consonants(example)}")
    print(f"   funstrings.word_count('{example}') = {funstrings.word_count(example)}")

    print("\n3. String Transformation")
    print(f"   funstrings.reverse_string('{example}') = '{funstrings.reverse_string(example)}'")
    print(f"   funstrings.sort_characters('{example}') = '{funstrings.sort_characters(example)}'")
    print(f"   funstrings.remove_whitespace('{example}') = '{funstrings.remove_whitespace(example)}'")

    print("\n4. String Analysis")
    print(f"   funstrings.is_palindrome('{example}') = {funstrings.is_palindrome(example)}")

    palindrome = "A man, a plan, a canal: Panama"
    print(f"   funstrings.is_palindrome('{palindrome}') = {funstrings.is_palindrome(palindrome)}")

def exercises():
    """Provide exercises for practice."""
    print_section("EXERCISES")

    print("Try these exercises to practice what you've learned:")

    print("\nExercise 1: Count the number of vowels and consonants in your name.")
    print("  Hint: Use funstrings.count_vowels() and funstrings.count_consonants()")

    print("\nExercise 2: Check if these phrases are palindromes:")
    print("  a) 'race car'")
    print("  b) 'hello world'")
    print("  c) 'Madam, I'm Adam'")
    print("  Hint: Use funstrings.is_palindrome()")

    print("\nExercise 3: Create a function that takes a sentence and returns:")
    print("  a) The sentence with all vowels removed")
    print("  b) The sentence with all consonants removed")
    print("  Hint: Use a loop and check each character")

    print("\nExercise 4: Create a function that counts how many times each word appears in a text.")
    print("  Hint: Split the text into words and use a dictionary to count occurrences")

def main():
    """Run the tutorial."""
    print("\nWELCOME TO THE STRING MANIPULATION BASICS TUTORIAL")
    print("This tutorial will teach you the basics of string manipulation in Python.")

    introduction()
    basic_operations()
    using_stringfun()
    exercises()

    print("\nCongratulations! You've completed the String Manipulation Basics Tutorial.")
    print("Keep practicing and exploring the FunStrings package to improve your skills.")

if __name__ == "__main__":
    main()
