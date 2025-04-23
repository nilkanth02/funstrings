import sys
from .operations import (
    reverse_string,
    count_vowels,
    count_consonants,
    is_palindrome,
    to_upper,
    to_lower,
    word_count,
    sort_characters,
    remove_whitespace,
)

def main():
    if len(sys.argv) < 2:
        print("Usage: python -m funstrings 'your string here'")
        sys.exit(1)

    s = sys.argv[1]
    print("Original String:          ", s)
    print("Reversed String:          ", reverse_string(s))
    print("Uppercase:                ", to_upper(s))
    print("Lowercase:                ", to_lower(s))
    print("Vowel Count:              ", count_vowels(s))
    print("Consonant Count:          ", count_consonants(s))
    print("Word Count:               ", word_count(s))
    print("Sorted Characters:        ", sort_characters(s))
    print("Sorted (Descending):      ", sort_characters(s, reverse=True))
    print("Without Whitespace:       ", remove_whitespace(s))
    print("Is Palindrome:            ", is_palindrome(s))

if __name__ == "__main__":
    main()
