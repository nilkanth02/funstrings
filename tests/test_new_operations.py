"""
Tests for the new string operations in the funstrings package.
"""

import pytest
import random
from funstrings import (
    # Text Analysis Functions
    get_word_frequencies,
    longest_word,
    shortest_word,
    average_word_length,
    is_pangram,

    # String Transformation Functions
    snake_to_camel,
    camel_to_snake,
    rotate_string,
    shuffle_string,
    reverse_words,

    # Pattern-based Functions
    extract_numbers,
    extract_emails,
    extract_urls,
    mask_sensitive,
    find_repeated_words,
)

# Set random seed for reproducible tests
random.seed(42)

# ===== Text Analysis Tests =====

def test_get_word_frequencies():
    assert get_word_frequencies("") == {}
    assert get_word_frequencies("hello") == {"hello": 1}
    assert get_word_frequencies("hello world hello") == {"hello": 2, "world": 1}
    assert get_word_frequencies("Hello HELLO hello") == {"hello": 3}  # Case insensitive

def test_longest_word():
    assert longest_word("") == ""
    assert longest_word("hello") == "hello"
    assert longest_word("hello amazing world") == "amazing"
    assert longest_word("one two three four") == "three"  # First one if tied

def test_shortest_word():
    assert shortest_word("") == ""
    assert shortest_word("hello") == "hello"
    assert shortest_word("hello a world") == "a"
    assert shortest_word("one two a b c") == "a"  # First one if tied

def test_average_word_length():
    assert average_word_length("") == 0.0
    assert average_word_length("hello") == 5.0
    assert average_word_length("hello world") == 5.0
    assert average_word_length("a bb ccc") == 2.0

def test_is_pangram():
    assert is_pangram("") == False
    assert is_pangram("hello world") == False
    assert is_pangram("The quick brown fox jumps over the lazy dog") == True
    assert is_pangram("Pack my box with five dozen liquor jugs") == True
    assert is_pangram("AbCdEfGhIjKlMnOpQrStUvWxYz") == True

# ===== String Transformation Tests =====

def test_snake_to_camel():
    assert snake_to_camel("") == ""
    assert snake_to_camel("hello") == "hello"
    assert snake_to_camel("hello_world") == "helloWorld"
    assert snake_to_camel("hello_world_example") == "helloWorldExample"
    assert snake_to_camel("a_b_c") == "aBC"

def test_camel_to_snake():
    assert camel_to_snake("") == ""
    assert camel_to_snake("hello") == "hello"
    assert camel_to_snake("helloWorld") == "hello_world"
    assert camel_to_snake("helloWorldExample") == "hello_world_example"
    assert camel_to_snake("ABC") == "a_b_c"

def test_rotate_string():
    assert rotate_string("", 5) == ""
    assert rotate_string("hello", 0) == "hello"
    assert rotate_string("hello", 2) == "lohel"
    assert rotate_string("hello", -1) == "elloh"
    assert rotate_string("hello", 5) == "hello"  # Full rotation
    assert rotate_string("hello", 7) == "lohel"  # Modulo length

def test_shuffle_string():
    # Since shuffle is random, we can only test that:
    # 1. The length is the same
    # 2. The characters are the same (just in different order)
    s = "hello"
    shuffled = shuffle_string(s)
    assert len(shuffled) == len(s)
    assert sorted(shuffled) == sorted(s)

    # With fixed seed, we can test exact output
    random.seed(42)
    assert shuffle_string("hello") == "leloh"

def test_reverse_words():
    assert reverse_words("") == ""
    assert reverse_words("hello") == "hello"
    assert reverse_words("hello world") == "world hello"
    assert reverse_words("one two three") == "three two one"
    assert reverse_words("   spaced   words   ") == "words spaced"

# ===== Pattern-based Tests =====

def test_extract_numbers():
    assert extract_numbers("") == []
    assert extract_numbers("hello world") == []
    assert extract_numbers("There are 42 apples and 15 oranges.") == ["42", "15"]
    assert extract_numbers("1 2 3 4 5") == ["1", "2", "3", "4", "5"]
    assert extract_numbers("Price: $1,234.56") == ["1", "234", "56"]

def test_extract_emails():
    assert extract_emails("") == []
    assert extract_emails("hello world") == []
    assert extract_emails("Contact us at info@example.com") == ["info@example.com"]
    assert extract_emails("Multiple emails: a@b.com, c@d.org, e@f.net") == ["a@b.com", "c@d.org", "e@f.net"]
    assert extract_emails("Invalid email: not.an.email") == []

def test_extract_urls():
    assert extract_urls("") == []
    assert extract_urls("hello world") == []
    assert extract_urls("Visit https://example.com") == ["https://example.com"]
    assert extract_urls("Multiple URLs: http://a.com and https://b.org") == ["http://a.com", "https://b.org"]
    assert extract_urls("Complex URL: https://example.com/path?query=value#fragment") == ["https://example.com/path?query=value#fragment"]

def test_mask_sensitive():
    assert mask_sensitive("", 4) == ""
    assert mask_sensitive("1234", 4) == "1234"
    assert mask_sensitive("1234567890", 4) == "******7890"
    assert mask_sensitive("1234567890", 0) == "**********"
    assert mask_sensitive("1234567890", 10) == "1234567890"

def test_find_repeated_words():
    assert find_repeated_words("") == []
    assert find_repeated_words("hello world") == []
    assert find_repeated_words("hello world hello") == ["hello"]
    assert find_repeated_words("one two one two three") == ["one", "two"]
    assert find_repeated_words("ONE one One") == ["one"]  # Case insensitive
