#!/usr/bin/env python
"""
Version 0.1.1 Functions Demo for FunStrings Package

This script demonstrates the new functions added in version 0.1.1 of the FunStrings package.
It's organized by function category for easy understanding.
"""

import funstrings

def print_section(title):
    """Helper function to print a section title."""
    print("\n" + "=" * 60)
    print(f" {title} ".center(60, "="))
    print("=" * 60)

def demo_data_cleaning():
    """Demonstrate the data cleaning functions."""
    print_section("DATA CLEANING FUNCTIONS")

    # HTML cleaning
    html_text = "<p>Hello <b>World</b>!</p><script>alert('test');</script>"
    print(f"Original HTML: '{html_text}'")
    print(f"Cleaned HTML: '{funstrings.remove_html_tags(html_text)}'")

    # Emoji removal
    emoji_text = "Hello 😊 World 🌍!"
    print(f"\nText with emojis: '{emoji_text}'")
    print(f"Text without emojis: '{funstrings.remove_emojis(emoji_text)}'")

    # Special character removal
    special_text = "Hello, World! This is a test #123."
    print(f"\nText with special chars: '{special_text}'")
    print(f"Alphanumeric only: '{funstrings.remove_special_characters(special_text)}'")

    # Contraction expansion
    contractions = "I don't know what I'm doing, but I'll figure it out."
    print(f"\nText with contractions: '{contractions}'")
    print(f"Expanded: '{funstrings.expand_contractions(contractions)}'")

    # Whitespace correction
    messy_text = "Hello   World!\t\nThis  is  messy."
    print(f"\nText with messy whitespace: '{messy_text}'")
    print(f"Corrected: '{funstrings.correct_whitespace(messy_text)}'")

def demo_text_analysis_helpers():
    """Demonstrate the text analysis helper functions."""
    print_section("TEXT ANALYSIS HELPER FUNCTIONS")

    sample_text = "The quick brown fox jumps over the lazy dog. The fox is quick and brown."
    print(f"Sample text: '{sample_text}'")

    # Unique words
    print("\n1. Unique Words")
    unique = funstrings.unique_words(sample_text)
    print(f"   Unique words: {unique}")

    # Most common word
    print("\n2. Most Common Word")
    common = funstrings.most_common_word(sample_text)
    print(f"   Most common word: '{common}'")

    # Sentence count
    print("\n3. Sentence Count")
    count = funstrings.sentence_count(sample_text)
    print(f"   Number of sentences: {count}")

    # Average sentence length
    print("\n4. Average Sentence Length")
    avg_length = funstrings.average_sentence_length(sample_text)
    print(f"   Average words per sentence: {avg_length:.2f}")

    # Character ratio
    print("\n5. Character Ratio")
    text_for_ratio = "Hello123 WORLD!"
    print(f"   Text: '{text_for_ratio}'")
    ratio = funstrings.character_ratio(text_for_ratio)
    print(f"   Uppercase ratio: {ratio['uppercase']:.2f}")
    print(f"   Lowercase ratio: {ratio['lowercase']:.2f}")
    print(f"   Numeric ratio: {ratio['numeric']:.2f}")

def demo_nlp_preprocessing():
    """Demonstrate the ML/NLP preprocessing functions."""
    print_section("ML/NLP PREPROCESSING FUNCTIONS")

    # N-grams
    text = "hello world"
    print(f"Text: '{text}'")
    print("\n1. N-grams")
    print(f"   Character bigrams for 'hello': {funstrings.generate_ngrams('hello', 2)}")
    print(f"   Word bigrams: {funstrings.generate_ngrams(text, 2)}")

    # Accent stripping
    accented = "café résumé naïve"
    print(f"\n2. Accent Stripping")
    print(f"   Original: '{accented}'")
    print(f"   Without accents: '{funstrings.strip_accents(accented)}'")

    # Lemmatization
    text_to_lemmatize = "running cats and dogs are jumping"
    print(f"\n3. Lemmatization")
    print(f"   Original: '{text_to_lemmatize}'")
    print(f"   Lemmatized: '{funstrings.lemmatize_text(text_to_lemmatize)}'")

    # ASCII check
    print(f"\n4. ASCII Check")
    print(f"   'Hello' is ASCII: {funstrings.is_ascii('Hello')}")
    print(f"   'café' is ASCII: {funstrings.is_ascii('café')}")

def demo_validation():
    """Demonstrate the validation functions."""
    print_section("VALIDATION FUNCTIONS")

    # Email validation
    print("1. Email Validation")
    emails = ["user@example.com", "invalid-email", "user.name+tag@example.co.uk"]
    for email in emails:
        print(f"   '{email}' is valid: {funstrings.is_valid_email(email)}")

    # URL validation
    print("\n2. URL Validation")
    urls = ["https://example.com", "example.com", "http://test.org/path?query=1"]
    for url in urls:
        print(f"   '{url}' is valid: {funstrings.is_valid_url(url)}")

    # IP validation
    print("\n3. IP Address Validation")
    ips = ["192.168.1.1", "2001:0db8:85a3:0000:0000:8a2e:0370:7334", "999.999.999.999"]
    for ip in ips:
        print(f"   '{ip}' is valid: {funstrings.is_valid_ip(ip)}")

    # Date validation
    print("\n4. Date Validation")
    dates = [
        ("2023-01-15", "%Y-%m-%d"),
        ("01/15/2023", "%m/%d/%Y"),
        ("2023-13-15", "%Y-%m-%d")
    ]
    for date, format in dates:
        print(f"   '{date}' in format '{format}' is valid: {funstrings.is_valid_date(date, format)}")

    # Special character check
    print("\n5. Special Character Check")
    texts = ["Hello World", "Hello, World!", "123ABC"]
    for text in texts:
        print(f"   '{text}' contains special chars: {funstrings.contains_special_characters(text)}")

def main():
    """Run the demonstration of all new functions."""
    print("FUNSTRINGS PACKAGE - VERSION 0.1.1 FUNCTIONS DEMONSTRATION")
    print("This script demonstrates the new functions added in version 0.1.1.")

    demo_data_cleaning()
    demo_text_analysis_helpers()
    demo_nlp_preprocessing()
    demo_validation()

    print("\nEnd of demonstration.")

if __name__ == "__main__":
    main()
