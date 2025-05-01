"""
Tests for the new functions added in v0.1.1 of the funstrings package.
"""

import pytest
import re
from funstrings import (
    # Data Cleaning Functions
    remove_html_tags,
    remove_emojis,
    remove_special_characters,
    expand_contractions,
    correct_whitespace,

    # Text Analysis Helpers
    unique_words,
    most_common_word,
    sentence_count,
    average_sentence_length,
    character_ratio,

    # ML/NLP Preprocessing
    generate_ngrams,
    strip_accents,
    lemmatize_text,
    is_ascii,

    # Validation Functions
    is_valid_email,
    is_valid_url,
    is_valid_ip,
    is_valid_date,
    contains_special_characters,
)

# ===== Data Cleaning Functions Tests =====

def test_remove_html_tags():
    assert remove_html_tags("<p>Hello</p>") == "Hello"
    assert remove_html_tags("<p>Hello <b>World</b></p>") == "Hello World"
    assert remove_html_tags("No HTML here") == "No HTML here"
    assert remove_html_tags("<a href='https://example.com'>Link</a>") == "Link"
    assert remove_html_tags("<script>alert('test');</script>") == ""

def test_remove_emojis():
    # Note: These tests may not display correctly in all editors
    assert remove_emojis("Hello 😊") == "Hello "
    assert remove_emojis("No emojis here") == "No emojis here"
    assert remove_emojis("🌍 Earth") == " Earth"
    assert remove_emojis("Multiple 🌟 emojis 🎉 here") == "Multiple  emojis  here"

def test_remove_special_characters():
    assert remove_special_characters("Hello, World!") == "HelloWorld"
    assert remove_special_characters("abc123") == "abc123"
    assert remove_special_characters("a@b#c$1%2^3") == "abc123"
    assert remove_special_characters("") == ""
    assert remove_special_characters("!@#$%^&*()") == ""

def test_expand_contractions():
    assert expand_contractions("don't") == "do not"
    assert expand_contractions("I can't do this") == "I cannot do this"
    assert expand_contractions("I'll see you're right") == "I will see you are right"
    assert expand_contractions("No contractions") == "No contractions"
    assert expand_contractions("won't, can't, shouldn't") == "will not, cannot, should not"

def test_correct_whitespace():
    assert correct_whitespace("  Hello  World  ") == "Hello World"
    assert correct_whitespace("Line1\nLine2\tTab") == "Line1 Line2 Tab"
    assert correct_whitespace("Too    many    spaces") == "Too many spaces"
    assert correct_whitespace("") == ""
    assert correct_whitespace("\t\n\r\f\v") == ""

# ===== Text Analysis Helpers Tests =====

def test_unique_words():
    assert unique_words("hello world hello python") == ["hello", "world", "python"]
    assert unique_words("") == []
    assert unique_words("one") == ["one"]
    assert unique_words("ONE one ONE") == ["one"]  # Case insensitive
    assert unique_words("a b c a b c") == ["a", "b", "c"]

def test_most_common_word():
    assert most_common_word("hello world hello python world hello") == "hello"
    assert most_common_word("one two three") == "one"  # First if tied
    assert most_common_word("") == ""
    assert most_common_word("a a a b b c") == "a"

def test_sentence_count():
    assert sentence_count("Hello world! How are you? I'm fine.") == 3
    assert sentence_count("One sentence only.") == 1
    assert sentence_count("No sentence ending") == 0
    assert sentence_count("") == 0
    assert sentence_count("Multiple! Sentences! With! Exclamations!") == 4

def test_average_sentence_length():
    assert average_sentence_length("Hello world! This is a test.") == 3.0
    assert average_sentence_length("One. Two. Three.") == 1.0
    assert average_sentence_length("") == 0.0
    # The function counts "Five words in a single sentence" as 6 words
    assert average_sentence_length("Five words in a single sentence.") == 6.0

def test_character_ratio():
    result = character_ratio("Hello123")
    assert result["uppercase"] == 1/8
    assert result["lowercase"] == 4/8
    assert result["numeric"] == 3/8

    assert character_ratio("") == {"uppercase": 0.0, "lowercase": 0.0, "numeric": 0.0}
    assert character_ratio("ABC") == {"uppercase": 1.0, "lowercase": 0.0, "numeric": 0.0}
    assert character_ratio("abc") == {"uppercase": 0.0, "lowercase": 1.0, "numeric": 0.0}
    assert character_ratio("123") == {"uppercase": 0.0, "lowercase": 0.0, "numeric": 1.0}

# ===== ML/NLP Preprocessing Tests =====

def test_generate_ngrams():
    assert generate_ngrams("hello", 2) == ["he", "el", "ll", "lo"]
    assert generate_ngrams("hello world", 2) == ["hello world"]
    assert generate_ngrams("a b c d", 2) == ["a b", "b c", "c d"]
    assert generate_ngrams("a b c d", 3) == ["a b c", "b c d"]
    assert generate_ngrams("short", 10) == []  # n-gram size > string length
    assert generate_ngrams("", 2) == []

def test_strip_accents():
    assert strip_accents("café") == "cafe"
    assert strip_accents("résumé") == "resume"
    assert strip_accents("no accents") == "no accents"
    assert strip_accents("Crème Brûlée") == "Creme Brulee"
    assert strip_accents("") == ""

def test_lemmatize_text():
    assert lemmatize_text("running") == "run"
    assert lemmatize_text("cats and dogs") == "cat and dog"
    assert lemmatize_text("walked") == "walk"
    assert lemmatize_text("flies") == "fly"
    assert lemmatize_text("boxes") == "box"
    assert lemmatize_text("") == ""

def test_is_ascii():
    assert is_ascii("Hello World") == True
    assert is_ascii("café") == False
    assert is_ascii("123") == True
    assert is_ascii("") == True
    assert is_ascii("résumé") == False

# ===== Validation Functions Tests =====

def test_is_valid_email():
    assert is_valid_email("user@example.com") == True
    assert is_valid_email("user.name+tag@example.co.uk") == True
    assert is_valid_email("invalid-email") == False
    assert is_valid_email("missing@tld") == False
    assert is_valid_email("") == False

def test_is_valid_url():
    assert is_valid_url("https://example.com") == True
    assert is_valid_url("http://example.com/path?query=1") == True
    assert is_valid_url("not-a-url") == False
    assert is_valid_url("example.com") == False  # Missing protocol
    assert is_valid_url("") == False

def test_is_valid_ip():
    assert is_valid_ip("192.168.1.1") == True
    assert is_valid_ip("2001:0db8:85a3:0000:0000:8a2e:0370:7334") == True
    assert is_valid_ip("not-an-ip") == False
    assert is_valid_ip("999.999.999.999") == False  # Invalid IPv4
    assert is_valid_ip("") == False

def test_is_valid_date():
    assert is_valid_date("2023-01-15") == True
    assert is_valid_date("01/15/2023", format="%m/%d/%Y") == True
    assert is_valid_date("not-a-date") == False
    assert is_valid_date("2023-13-15") == False  # Invalid month
    assert is_valid_date("") == False

def test_contains_special_characters():
    assert contains_special_characters("Hello!") == True
    assert contains_special_characters("HelloWorld123") == False
    assert contains_special_characters("@#$%^&*") == True
    assert contains_special_characters("") == False
    assert contains_special_characters("With Space") == False  # Space is not special
