# Getting Started with StringFun

This guide will help you get started with the StringFun package. It's designed to be beginner-friendly and educational.

## Installation

You can install StringFun using pip:

```bash
pip install stringfun
```

Or install directly from the source code:

```bash
git clone https://github.com/nilkanth02/stringfun.git
cd stringfun
pip install -e .
```

## Basic Usage

Here's a simple example of how to use StringFun:

```python
import stringfun

# Reverse a string
text = "Hello, World!"
reversed_text = stringfun.reverse_string(text)
print(reversed_text)  # Output: "!dlroW ,olleH"

# Count vowels and consonants
vowels = stringfun.count_vowels(text)
consonants = stringfun.count_consonants(text)
print(f"Vowels: {vowels}, Consonants: {consonants}")  # Output: "Vowels: 3, Consonants: 7"

# Check if a string is a palindrome
is_pal = stringfun.is_palindrome("A man, a plan, a canal: Panama")
print(is_pal)  # Output: True
```

## Available Functions

StringFun provides the following functions:

| Function | Description | Example |
|----------|-------------|---------|
| `reverse_string(s)` | Reverses a string | `reverse_string("hello")` → `"olleh"` |
| `count_vowels(s)` | Counts vowels in a string | `count_vowels("hello")` → `2` |
| `count_consonants(s)` | Counts consonants in a string | `count_consonants("hello")` → `3` |
| `is_palindrome(s)` | Checks if a string is a palindrome | `is_palindrome("racecar")` → `True` |
| `to_upper(s)` | Converts a string to uppercase | `to_upper("hello")` → `"HELLO"` |
| `to_lower(s)` | Converts a string to lowercase | `to_lower("HELLO")` → `"hello"` |
| `word_count(s)` | Counts words in a string | `word_count("hello world")` → `2` |
| `sort_characters(s, reverse=False)` | Sorts characters in a string | `sort_characters("hello")` → `"ehllo"` |
| `remove_whitespace(s)` | Removes whitespace from a string | `remove_whitespace("hello world")` → `"helloworld"` |

## For Students and Beginners

If you're new to Python or programming in general, here are some tips:

1. **Start with simple examples**: Try each function with simple inputs first
2. **Experiment**: Change the examples and see what happens
3. **Read the code**: Look at the implementation to understand how it works
4. **Build something**: Use these functions to build a simple text processing tool

## Next Steps

- Check out the [tutorials](../tutorials/) for more in-depth examples
- Look at the [examples](../examples/) for practical applications
- Read the [API documentation](./api.md) for detailed function descriptions
- Try the [exercises](../tutorials/string_manipulation_basics.py) to test your understanding
