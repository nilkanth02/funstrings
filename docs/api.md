# StringFun API Reference

This document provides detailed information about all the functions available in the StringFun package.

## Table of Contents

- [Basic String Operations](#basic-string-operations)
- [Text Analysis Functions](#text-analysis-functions)
- [String Transformation Functions](#string-transformation-functions)
- [Pattern-based Functions](#pattern-based-functions)
- [For Students and Beginners](#for-students-and-beginners)

## Basic String Operations

### reverse_string

```python
def reverse_string(s: str) -> str:
    """Returns the reversed version of the input string."""
```

**Parameters:**
- `s` (str): The input string to reverse

**Returns:**
- str: The reversed string

**Example:**
```python
from stringfun import reverse_string

text = "Hello, World!"
reversed_text = reverse_string(text)
print(reversed_text)  # Output: "!dlroW ,olleH"
```

### count_vowels

```python
def count_vowels(s: str) -> int:
    """Counts the number of vowels in the input string."""
```

**Parameters:**
- `s` (str): The input string to count vowels in

**Returns:**
- int: The number of vowels in the string

**Notes:**
- Vowels are defined as: 'a', 'e', 'i', 'o', 'u' (both uppercase and lowercase)

**Example:**
```python
from stringfun import count_vowels

text = "Hello, World!"
vowel_count = count_vowels(text)
print(vowel_count)  # Output: 3
```

### count_consonants

```python
def count_consonants(s: str) -> int:
    """Counts the number of consonants in the input string."""
```

**Parameters:**
- `s` (str): The input string to count consonants in

**Returns:**
- int: The number of consonants in the string

**Notes:**
- Consonants are defined as alphabetic characters that are not vowels

**Example:**
```python
from stringfun import count_consonants

text = "Hello, World!"
consonant_count = count_consonants(text)
print(consonant_count)  # Output: 7
```

### is_palindrome

```python
def is_palindrome(s: str) -> bool:
    """Checks if the input string is a palindrome.

    This function ignores case and non-alphanumeric characters.
    """
```

**Parameters:**
- `s` (str): The input string to check

**Returns:**
- bool: True if the string is a palindrome, False otherwise

**Notes:**
- The function ignores case (uppercase/lowercase)
- The function ignores non-alphanumeric characters (punctuation, spaces, etc.)

**Example:**
```python
from stringfun import is_palindrome

text1 = "racecar"
text2 = "A man, a plan, a canal: Panama"
text3 = "hello"

print(is_palindrome(text1))  # Output: True
print(is_palindrome(text2))  # Output: True
print(is_palindrome(text3))  # Output: False
```

### to_upper

```python
def to_upper(s: str) -> str:
    """Converts the input string to uppercase."""
```

**Parameters:**
- `s` (str): The input string to convert

**Returns:**
- str: The uppercase version of the input string

**Example:**
```python
from stringfun import to_upper

text = "Hello, World!"
upper_text = to_upper(text)
print(upper_text)  # Output: "HELLO, WORLD!"
```

### to_lower

```python
def to_lower(s: str) -> str:
    """Converts the input string to lowercase."""
```

**Parameters:**
- `s` (str): The input string to convert

**Returns:**
- str: The lowercase version of the input string

**Example:**
```python
from stringfun import to_lower

text = "Hello, World!"
lower_text = to_lower(text)
print(lower_text)  # Output: "hello, world!"
```

### word_count

```python
def word_count(s: str) -> int:
    """Counts the number of words in the input string."""
```

**Parameters:**
- `s` (str): The input string to count words in

**Returns:**
- int: The number of words in the string

**Notes:**
- Words are defined as sequences of characters separated by whitespace

**Example:**
```python
from stringfun import word_count

text = "The quick brown fox jumps over the lazy dog"
count = word_count(text)
print(count)  # Output: 9
```

### sort_characters

```python
def sort_characters(s: str, reverse: bool = False) -> str:
    """Sorts the characters of the input string alphabetically.

    If reverse is True, sorts in descending order.
    """
```

**Parameters:**
- `s` (str): The input string to sort
- `reverse` (bool, optional): If True, sort in descending order. Default is False.

**Returns:**
- str: The string with characters sorted alphabetically

**Example:**
```python
from stringfun import sort_characters

text = "Hello, World!"
sorted_text = sort_characters(text)
print(sorted_text)  # Output: " !,HWdellloor"

sorted_text_reverse = sort_characters(text, reverse=True)
print(sorted_text_reverse)  # Output: "roollledWH,! "
```

### remove_whitespace

```python
def remove_whitespace(s: str) -> str:
    """Removes all whitespace characters from the input string."""
```

**Parameters:**
- `s` (str): The input string to process

**Returns:**
- str: The string with all whitespace removed

**Example:**
```python
from stringfun import remove_whitespace

text = "Hello, World!  This is a test."
no_space_text = remove_whitespace(text)
print(no_space_text)  # Output: "Hello,World!Thisisatest."
```

## Text Analysis Functions

### get_word_frequencies

```python
def get_word_frequencies(s: str) -> Dict[str, int]:
    """Return frequency count of each word in the input string."""
```

**Parameters:**
- `s` (str): The input string to analyze

**Returns:**
- Dict[str, int]: A dictionary with words as keys and their frequencies as values

**Example:**
```python
from stringfun import get_word_frequencies

text = "hello world hello"
freq = get_word_frequencies(text)
print(freq)  # Output: {'hello': 2, 'world': 1}
```

### longest_word

```python
def longest_word(s: str) -> str:
    """Find the longest word in the input string."""
```

**Parameters:**
- `s` (str): The input string to analyze

**Returns:**
- str: The longest word in the string

**Notes:**
- If multiple words have the same maximum length, returns the first one

**Example:**
```python
from stringfun import longest_word

text = "hello amazing world"
word = longest_word(text)
print(word)  # Output: "amazing"
```

### shortest_word

```python
def shortest_word(s: str) -> str:
    """Find the shortest word in the input string."""
```

**Parameters:**
- `s` (str): The input string to analyze

**Returns:**
- str: The shortest word in the string

**Notes:**
- If multiple words have the same minimum length, returns the first one

**Example:**
```python
from stringfun import shortest_word

text = "hello a world"
word = shortest_word(text)
print(word)  # Output: "a"
```

### average_word_length

```python
def average_word_length(s: str) -> float:
    """Calculate the average word length in the input string."""
```

**Parameters:**
- `s` (str): The input string to analyze

**Returns:**
- float: The average length of words in the string, or 0.0 if no words

**Example:**
```python
from stringfun import average_word_length

text = "hello world"
avg = average_word_length(text)
print(avg)  # Output: 5.0
```

### is_pangram

```python
def is_pangram(s: str) -> bool:
    """Check if the input string contains all letters of the alphabet."""
```

**Parameters:**
- `s` (str): The input string to check

**Returns:**
- bool: True if the string is a pangram, False otherwise

**Notes:**
- A pangram is a sentence that contains every letter of the alphabet at least once
- This function is case-insensitive

**Example:**
```python
from stringfun import is_pangram

text = "The quick brown fox jumps over the lazy dog"
result = is_pangram(text)
print(result)  # Output: True
```

## String Transformation Functions

### snake_to_camel

```python
def snake_to_camel(s: str) -> str:
    """Convert snake_case string to camelCase."""
```

**Parameters:**
- `s` (str): The input snake_case string

**Returns:**
- str: The string converted to camelCase

**Example:**
```python
from stringfun import snake_to_camel

text = "hello_world_example"
result = snake_to_camel(text)
print(result)  # Output: "helloWorldExample"
```

### camel_to_snake

```python
def camel_to_snake(s: str) -> str:
    """Convert camelCase string to snake_case."""
```

**Parameters:**
- `s` (str): The input camelCase string

**Returns:**
- str: The string converted to snake_case

**Example:**
```python
from stringfun import camel_to_snake

text = "helloWorldExample"
result = camel_to_snake(text)
print(result)  # Output: "hello_world_example"
```

### rotate_string

```python
def rotate_string(s: str, n: int) -> str:
    """Rotate string by n positions."""
```

**Parameters:**
- `s` (str): The input string to rotate
- `n` (int): Number of positions to rotate (positive for right, negative for left)

**Returns:**
- str: The rotated string

**Example:**
```python
from stringfun import rotate_string

text = "hello"
right_rotated = rotate_string(text, 2)
print(right_rotated)  # Output: "lohel"

left_rotated = rotate_string(text, -1)
print(left_rotated)  # Output: "elloh"
```

### shuffle_string

```python
def shuffle_string(s: str) -> str:
    """Randomly shuffle the characters in the input string."""
```

**Parameters:**
- `s` (str): The input string to shuffle

**Returns:**
- str: A string with the characters randomly shuffled

**Notes:**
- The result will vary due to randomness

**Example:**
```python
from stringfun import shuffle_string

text = "hello"
shuffled = shuffle_string(text)
print(shuffled)  # Output will vary, e.g., "lhoel"
```

### reverse_words

```python
def reverse_words(s: str) -> str:
    """Reverse the order of words but not the letters within each word."""
```

**Parameters:**
- `s` (str): The input string

**Returns:**
- str: A string with the words in reverse order

**Example:**
```python
from stringfun import reverse_words

text = "hello world python"
result = reverse_words(text)
print(result)  # Output: "python world hello"
```

## Pattern-based Functions

### extract_numbers

```python
def extract_numbers(s: str) -> List[str]:
    """Extract all numbers from the input string."""
```

**Parameters:**
- `s` (str): The input string to extract numbers from

**Returns:**
- List[str]: A list of strings containing all numbers found

**Example:**
```python
from stringfun import extract_numbers

text = "There are 42 apples and 15 oranges."
numbers = extract_numbers(text)
print(numbers)  # Output: ['42', '15']
```

### extract_emails

```python
def extract_emails(s: str) -> List[str]:
    """Extract all email addresses from the input string."""
```

**Parameters:**
- `s` (str): The input string to extract emails from

**Returns:**
- List[str]: A list of strings containing all email addresses found

**Example:**
```python
from stringfun import extract_emails

text = "Contact us at info@example.com or support@example.org"
emails = extract_emails(text)
print(emails)  # Output: ['info@example.com', 'support@example.org']
```

### extract_urls

```python
def extract_urls(s: str) -> List[str]:
    """Extract all URLs from the input string."""
```

**Parameters:**
- `s` (str): The input string to extract URLs from

**Returns:**
- List[str]: A list of strings containing all URLs found

**Example:**
```python
from stringfun import extract_urls

text = "Visit https://example.com or http://test.org for more info."
urls = extract_urls(text)
print(urls)  # Output: ['https://example.com', 'http://test.org']
```

### mask_sensitive

```python
def mask_sensitive(s: str, chars: int = 4) -> str:
    """Mask all but the last n characters with asterisks."""
```

**Parameters:**
- `s` (str): The input string to mask
- `chars` (int, optional): Number of characters to leave unmasked at the end. Default is 4.

**Returns:**
- str: The masked string

**Example:**
```python
from stringfun import mask_sensitive

text = "1234567890"
masked = mask_sensitive(text, 4)
print(masked)  # Output: "******7890"
```

### find_repeated_words

```python
def find_repeated_words(s: str) -> List[str]:
    """Find all words that appear more than once in the input string."""
```

**Parameters:**
- `s` (str): The input string to analyze

**Returns:**
- List[str]: A list of words that appear multiple times

**Example:**
```python
from stringfun import find_repeated_words

text = "hello world hello python world code"
repeated = find_repeated_words(text)
print(repeated)  # Output: ['hello', 'world']
```

## For Students and Beginners

When using these functions, remember:

1. **Type Hints**: The type hints (like `str` and `int`) indicate what type of data the function expects and returns
2. **Docstrings**: The text in triple quotes is called a docstring and explains what the function does
3. **Parameters**: These are the inputs to the function
4. **Return Values**: These are the outputs from the function

To use any function, you need to:
1. Import it from the package
2. Call it with the appropriate parameters
3. Use the returned value as needed
