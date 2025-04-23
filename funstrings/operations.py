import re
import random
from collections import Counter
from typing import Dict, List

# ===== Basic String Operations =====

def reverse_string(s: str) -> str:
    """Returns the reversed version of the input string."""
    return s[::-1]

def count_vowels(s: str) -> int:
    """Counts the number of vowels in the input string."""
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

def count_consonants(s: str) -> int:
    """Counts the number of consonants in the input string."""
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char.isalpha() and char not in vowels)

def is_palindrome(s: str) -> bool:
    """Checks if the input string is a palindrome.

    This function ignores case and non-alphanumeric characters.
    """
    cleaned = re.sub(r'[^A-Za-z0-9]', '', s).lower()
    return cleaned == cleaned[::-1]

def to_upper(s: str) -> str:
    """Converts the input string to uppercase."""
    return s.upper()

def to_lower(s: str) -> str:
    """Converts the input string to lowercase."""
    return s.lower()

def word_count(s: str) -> int:
    """Counts the number of words in the input string."""
    return len(s.split())

def sort_characters(s: str, reverse: bool = False) -> str:
    """Sorts the characters of the input string alphabetically.

    If reverse is True, sorts in descending order.
    """
    return ''.join(sorted(s, reverse=reverse))

def remove_whitespace(s: str) -> str:
    """Removes all whitespace characters from the input string."""
    return ''.join(s.split())

# ===== Text Analysis Functions =====

def get_word_frequencies(s: str) -> Dict[str, int]:
    """Return frequency count of each word in the input string.

    Args:
        s: The input string to analyze

    Returns:
        A dictionary with words as keys and their frequencies as values

    Example:
        >>> get_word_frequencies("hello world hello")
        {'hello': 2, 'world': 1}
    """
    # Convert to lowercase and split into words
    words = s.lower().split()
    # Use Counter to count occurrences of each word
    return dict(Counter(words))

def longest_word(s: str) -> str:
    """Find the longest word in the input string.

    If multiple words have the same maximum length, returns the first one.

    Args:
        s: The input string to analyze

    Returns:
        The longest word in the string

    Example:
        >>> longest_word("hello amazing world")
        'amazing'
    """
    if not s.strip():
        return ""

    words = s.split()
    return max(words, key=len) if words else ""

def shortest_word(s: str) -> str:
    """Find the shortest word in the input string.

    If multiple words have the same minimum length, returns the first one.

    Args:
        s: The input string to analyze

    Returns:
        The shortest word in the string

    Example:
        >>> shortest_word("hello amazing a world")
        'a'
    """
    if not s.strip():
        return ""

    words = s.split()
    return min(words, key=len) if words else ""

def average_word_length(s: str) -> float:
    """Calculate the average word length in the input string.

    Args:
        s: The input string to analyze

    Returns:
        The average length of words in the string, or 0.0 if no words

    Example:
        >>> average_word_length("hello world")
        5.0
    """
    words = s.split()
    if not words:
        return 0.0

    total_length = sum(len(word) for word in words)
    return total_length / len(words)

def is_pangram(s: str) -> bool:
    """Check if the input string contains all letters of the alphabet.

    A pangram is a sentence that contains every letter of the alphabet at least once.
    This function is case-insensitive.

    Args:
        s: The input string to check

    Returns:
        True if the string is a pangram, False otherwise

    Example:
        >>> is_pangram("The quick brown fox jumps over the lazy dog")
        True
    """
    # Convert to lowercase and remove non-alphabetic characters
    letters = set(char.lower() for char in s if char.isalpha())
    # Check if all 26 letters of the alphabet are present
    return len(letters) == 26

# ===== String Transformation Functions =====

def snake_to_camel(s: str) -> str:
    """Convert snake_case string to camelCase.

    Args:
        s: The input snake_case string

    Returns:
        The string converted to camelCase

    Example:
        >>> snake_to_camel("hello_world_example")
        'helloWorldExample'
    """
    # Split by underscore and capitalize each word except the first
    words = s.split('_')
    return words[0] + ''.join(word.capitalize() for word in words[1:])

def camel_to_snake(s: str) -> str:
    """Convert camelCase string to snake_case.

    Args:
        s: The input camelCase string

    Returns:
        The string converted to snake_case

    Example:
        >>> camel_to_snake("helloWorldExample")
        'hello_world_example'
    """
    # Insert underscore before uppercase letters and convert to lowercase
    result = re.sub(r'(?<!^)(?=[A-Z])', '_', s).lower()
    return result

def rotate_string(s: str, n: int) -> str:
    """Rotate string by n positions.

    Positive n rotates right, negative n rotates left.

    Args:
        s: The input string to rotate
        n: Number of positions to rotate (positive for right, negative for left)

    Returns:
        The rotated string

    Example:
        >>> rotate_string("hello", 2)
        'lohel'
        >>> rotate_string("hello", -1)
        'elloh'
    """
    if not s:
        return ""

    # Handle negative rotation (left rotation)
    if n < 0:
        # For left rotation, we take from the beginning and append the rest
        n = -n % len(s)  # Convert to positive and ensure it's within string length
        return s[n:] + s[:n]
    else:
        # For right rotation, we take from the end and prepend to the beginning
        n = n % len(s)  # Ensure n is within string length
        return s[len(s)-n:] + s[:len(s)-n]

def shuffle_string(s: str) -> str:
    """Randomly shuffle the characters in the input string.

    Args:
        s: The input string to shuffle

    Returns:
        A string with the characters randomly shuffled

    Example:
        >>> # Result will vary due to randomness
        >>> shuffle_string("hello")
        'lhoel'
    """
    # Convert to list, shuffle, and join back to string
    char_list = list(s)
    random.shuffle(char_list)
    return ''.join(char_list)

def reverse_words(s: str) -> str:
    """Reverse the order of words but not the letters within each word.

    Args:
        s: The input string

    Returns:
        A string with the words in reverse order

    Example:
        >>> reverse_words("hello world python")
        'python world hello'
    """
    # Split into words, reverse the list, and join back with spaces
    return ' '.join(s.split()[::-1])

# ===== Pattern-based Functions =====

def extract_numbers(s: str) -> List[str]:
    """Extract all numbers from the input string.

    Args:
        s: The input string to extract numbers from

    Returns:
        A list of strings containing all numbers found

    Example:
        >>> extract_numbers("There are 42 apples and 15 oranges.")
        ['42', '15']
    """
    return re.findall(r'\d+', s)

def extract_emails(s: str) -> List[str]:
    """Extract all email addresses from the input string.

    Args:
        s: The input string to extract emails from

    Returns:
        A list of strings containing all email addresses found

    Example:
        >>> extract_emails("Contact us at info@example.com or support@example.org")
        ['info@example.com', 'support@example.org']
    """
    # Simple regex for email extraction - not perfect but works for common formats
    return re.findall(r'[\w.+-]+@[\w-]+\.[\w.-]+', s)

def extract_urls(s: str) -> List[str]:
    """Extract all URLs from the input string.

    Args:
        s: The input string to extract URLs from

    Returns:
        A list of strings containing all URLs found

    Example:
        >>> extract_urls("Visit https://example.com or http://test.org for more info.")
        ['https://example.com', 'http://test.org']
    """
    # Simple regex for URL extraction - handles common formats
    return re.findall(r'https?://[\w.-]+(?:\.[\w.-]+)+[\w\-._~:/?#[\]@!$&\'()*+,;=]*', s)

def mask_sensitive(s: str, chars: int = 4) -> str:
    """Mask all but the last n characters with asterisks.

    Args:
        s: The input string to mask
        chars: Number of characters to leave unmasked at the end (default: 4)

    Returns:
        The masked string

    Example:
        >>> mask_sensitive("1234567890", 4)
        '******7890'
    """
    if not s:
        return ""

    if chars == 0:
        return '*' * len(s)

    if len(s) <= chars:
        return s

    return '*' * (len(s) - chars) + s[-chars:]

def find_repeated_words(s: str) -> List[str]:
    """Find all words that appear more than once in the input string.

    Args:
        s: The input string to analyze

    Returns:
        A list of words that appear multiple times

    Example:
        >>> find_repeated_words("hello world hello python world code")
        ['hello', 'world']
    """
    # Get word frequencies and filter for those appearing more than once
    word_freq = get_word_frequencies(s)
    return [word for word, count in word_freq.items() if count > 1]
