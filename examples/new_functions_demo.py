#!/usr/bin/env python
"""
New Functions Demo for FunStrings Package

This script demonstrates the new functions added to the FunStrings package.
It's organized by function category for easy understanding.
"""

import funstrings

def print_section(title):
    """Helper function to print a section title."""
    print("\n" + "=" * 60)
    print(f" {title} ".center(60, "="))
    print("=" * 60)

def demo_text_analysis():
    """Demonstrate the text analysis functions."""
    print_section("TEXT ANALYSIS FUNCTIONS")

    sample_text = "The quick brown fox jumps over the lazy dog. The fox is quick and brown."

    print(f"Sample text: '{sample_text}'")
    print("\n1. Word Frequencies")
    frequencies = funstrings.get_word_frequencies(sample_text)
    for word, count in sorted(frequencies.items(), key=lambda x: x[1], reverse=True):
        print(f"   '{word}': {count}")

    print("\n2. Longest and Shortest Words")
    print(f"   Longest word: '{funstrings.longest_word(sample_text)}'")
    print(f"   Shortest word: '{funstrings.shortest_word(sample_text)}'")

    print("\n3. Average Word Length")
    print(f"   Average: {funstrings.average_word_length(sample_text):.2f} characters")

    print("\n4. Pangram Check")
    print(f"   Is pangram: {funstrings.is_pangram(sample_text)}")
    print(f"   Another example: 'Pack my box with five dozen liquor jugs'")
    print(f"   Is pangram: {funstrings.is_pangram('Pack my box with five dozen liquor jugs')}")

def demo_transformations():
    """Demonstrate the string transformation functions."""
    print_section("STRING TRANSFORMATION FUNCTIONS")

    print("1. Snake Case <-> Camel Case")
    snake = "hello_world_example"
    camel = "helloWorldExample"
    print(f"   Snake case: '{snake}'")
    print(f"   To camel case: '{funstrings.snake_to_camel(snake)}'")
    print(f"   Camel case: '{camel}'")
    print(f"   To snake case: '{funstrings.camel_to_snake(camel)}'")

    print("\n2. String Rotation")
    text = "hello"
    print(f"   Original: '{text}'")
    print(f"   Rotate right by 2: '{funstrings.rotate_string(text, 2)}'")
    print(f"   Rotate left by 1: '{funstrings.rotate_string(text, -1)}'")

    print("\n3. String Shuffling")
    print(f"   Original: '{text}'")
    print(f"   Shuffled: '{funstrings.shuffle_string(text)}'")
    print(f"   Note: Result will vary due to randomness")

    print("\n4. Reverse Words")
    sentence = "Python is an amazing language"
    print(f"   Original: '{sentence}'")
    print(f"   Reversed words: '{funstrings.reverse_words(sentence)}'")

def demo_pattern_based():
    """Demonstrate the pattern-based functions."""
    print_section("PATTERN-BASED FUNCTIONS")

    # Sample text with various patterns
    sample = """
    Contact us at info@example.com or support@example.org.
    Visit our website at https://example.com or http://test.org.
    There are 42 apples and 15 oranges in the basket.
    Credit card: 1234 5678 9012 3456
    """

    print(f"Sample text:\n{sample}")

    print("\n1. Extract Numbers")
    numbers = funstrings.extract_numbers(sample)
    print(f"   Numbers found: {numbers}")

    print("\n2. Extract Emails")
    emails = funstrings.extract_emails(sample)
    print(f"   Emails found: {emails}")

    print("\n3. Extract URLs")
    urls = funstrings.extract_urls(sample)
    print(f"   URLs found: {urls}")

    print("\n4. Mask Sensitive Data")
    card = "1234567890123456"
    print(f"   Original: '{card}'")
    print(f"   Masked (last 4): '{funstrings.mask_sensitive(card, 4)}'")
    print(f"   Masked (last 6): '{funstrings.mask_sensitive(card, 6)}'")

    print("\n5. Find Repeated Words")
    text = "The quick brown fox jumps over the lazy dog. The fox is quick."
    print(f"   Text: '{text}'")
    repeated = funstrings.find_repeated_words(text)
    print(f"   Repeated words: {repeated}")

def main():
    """Run the demonstration of all new functions."""
    print("FUNSTRINGS PACKAGE - NEW FUNCTIONS DEMONSTRATION")
    print("This script demonstrates the new functions added to the FunStrings package.")

    demo_text_analysis()
    demo_transformations()
    demo_pattern_based()

    print("\nEnd of demonstration.")

if __name__ == "__main__":
    main()
