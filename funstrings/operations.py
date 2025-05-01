import re
import random
import string
import unicodedata
import ipaddress
import datetime
from collections import Counter
from typing import Dict, List, Tuple, Optional, Union, Set

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

# ===== Data Cleaning Functions =====

def remove_html_tags(s: str) -> str:
    """Strip all HTML tags from the input string.

    Args:
        s: The input string containing HTML tags

    Returns:
        String with all HTML tags removed

    Example:
        >>> remove_html_tags("<p>Hello <b>World</b></p>")
        'Hello World'
    """
    # First remove script and style elements completely (content and tags)
    s = re.sub(r'<script.*?</script>', '', s, flags=re.DOTALL)
    s = re.sub(r'<style.*?</style>', '', s, flags=re.DOTALL)
    # Then remove remaining tags
    return re.sub(r'<[^>]+>', '', s)

def remove_emojis(s: str) -> str:
    """Remove emojis from the input string.

    Args:
        s: The input string potentially containing emojis

    Returns:
        String with all emojis removed

    Example:
        >>> remove_emojis("Hello 😊 World 🌍")
        'Hello  World '
    """
    # This pattern matches most emoji characters
    emoji_pattern = re.compile(
        "["
        "\U0001F600-\U0001F64F"  # emoticons
        "\U0001F300-\U0001F5FF"  # symbols & pictographs
        "\U0001F680-\U0001F6FF"  # transport & map symbols
        "\U0001F700-\U0001F77F"  # alchemical symbols
        "\U0001F780-\U0001F7FF"  # Geometric Shapes
        "\U0001F800-\U0001F8FF"  # Supplemental Arrows-C
        "\U0001F900-\U0001F9FF"  # Supplemental Symbols and Pictographs
        "\U0001FA00-\U0001FA6F"  # Chess Symbols
        "\U0001FA70-\U0001FAFF"  # Symbols and Pictographs Extended-A
        "\U00002702-\U000027B0"  # Dingbats
        "\U000024C2-\U0001F251"
        "]+", flags=re.UNICODE
    )
    return emoji_pattern.sub(r'', s)

def remove_special_characters(s: str) -> str:
    """Keep only letters and numbers, removing all special characters.

    Args:
        s: The input string

    Returns:
        String with only alphanumeric characters

    Example:
        >>> remove_special_characters("Hello, World! 123")
        'HelloWorld123'
    """
    return re.sub(r'[^a-zA-Z0-9]', '', s)

def expand_contractions(s: str) -> str:
    """Expand common English contractions (e.g., "don't" to "do not").

    Args:
        s: The input string with contractions

    Returns:
        String with contractions expanded

    Example:
        >>> expand_contractions("I don't know what I'm doing")
        'I do not know what I am doing'
    """
    # Dictionary of common contractions
    contractions = {
        "ain't": "am not",
        "aren't": "are not",
        "can't": "cannot",
        "couldn't": "could not",
        "didn't": "did not",
        "doesn't": "does not",
        "don't": "do not",
        "hadn't": "had not",
        "hasn't": "has not",
        "haven't": "have not",
        "he'd": "he would",
        "he'll": "he will",
        "he's": "he is",
        "i'd": "I would",
        "i'll": "I will",
        "i'm": "I am",
        "i've": "I have",
        "isn't": "is not",
        "it's": "it is",
        "let's": "let us",
        "mustn't": "must not",
        "shan't": "shall not",
        "she'd": "she would",
        "she'll": "she will",
        "she's": "she is",
        "shouldn't": "should not",
        "that's": "that is",
        "there's": "there is",
        "they'd": "they would",
        "they'll": "they will",
        "they're": "they are",
        "they've": "they have",
        "we'd": "we would",
        "we're": "we are",
        "we've": "we have",
        "weren't": "were not",
        "what'll": "what will",
        "what're": "what are",
        "what's": "what is",
        "what've": "what have",
        "where's": "where is",
        "who'd": "who would",
        "who'll": "who will",
        "who're": "who are",
        "who's": "who is",
        "who've": "who have",
        "won't": "will not",
        "wouldn't": "would not",
        "you'd": "you would",
        "you'll": "you will",
        "you're": "you are",
        "you've": "you have",
    }

    # Function to replace contractions in a match
    def replace(match):
        return contractions[match.group(0).lower()]

    # Pattern to match contractions
    pattern = re.compile(r'\b(' + '|'.join(contractions.keys()) + r')\b', re.IGNORECASE)

    return pattern.sub(replace, s)

def correct_whitespace(s: str) -> str:
    """Remove excessive whitespace, normalize tabs and newlines.

    Args:
        s: The input string with potentially messy whitespace

    Returns:
        String with normalized whitespace

    Example:
        >>> correct_whitespace("Hello   World\\t\\n  !")
        'Hello World !'
    """
    # Replace tabs and newlines with spaces
    s = re.sub(r'[\t\n\r\f\v]', ' ', s)
    # Replace multiple spaces with a single space
    s = re.sub(r' +', ' ', s)
    # Trim leading and trailing whitespace
    return s.strip()

# ===== Text Analysis Helpers =====

def unique_words(s: str) -> List[str]:
    """Return a list of unique words in the input string.

    Args:
        s: The input string to analyze

    Returns:
        List of unique words (case-insensitive)

    Example:
        >>> unique_words("hello world hello python")
        ['hello', 'world', 'python']
    """
    # Convert to lowercase and split into words
    words = s.lower().split()
    # Return unique words while preserving original order
    return list(dict.fromkeys(words))

def most_common_word(s: str) -> str:
    """Return the most frequently occurring word in the input string.

    If multiple words have the same highest frequency, returns the first one.

    Args:
        s: The input string to analyze

    Returns:
        The most common word, or empty string if input is empty

    Example:
        >>> most_common_word("hello world hello python world hello")
        'hello'
    """
    if not s.strip():
        return ""

    # Get word frequencies
    word_freq = get_word_frequencies(s)
    if not word_freq:
        return ""

    # Find the word with the highest frequency
    return max(word_freq.items(), key=lambda x: x[1])[0]

def sentence_count(s: str) -> int:
    """Count the number of sentences in the input string.

    Sentences are determined by the presence of sentence-ending punctuation
    (.!?) followed by a space or end of string.

    Args:
        s: The input string to analyze

    Returns:
        Number of sentences detected

    Example:
        >>> sentence_count("Hello world! How are you? I'm fine.")
        3
    """
    if not s.strip():
        return 0

    # Count sentences by looking for sentence-ending punctuation
    # This is a simple approach and may not handle all cases perfectly
    return len(re.findall(r'[.!?](?:\s|$)', s))

def average_sentence_length(s: str) -> float:
    """Calculate the average number of words per sentence.

    Args:
        s: The input string to analyze

    Returns:
        Average words per sentence, or 0.0 if no sentences

    Example:
        >>> average_sentence_length("Hello world! This is a test.")
        3.0
    """
    # If the string is empty, return 0.0
    if not s.strip():
        return 0.0

    # Split the text into sentences
    sentences = re.split(r'[.!?](?:\s|$)', s.strip())
    # Remove empty sentences (e.g., from trailing punctuation)
    sentences = [sent.strip() for sent in sentences if sent.strip()]

    if not sentences:
        return 0.0

    # Count words in each sentence
    word_counts = []
    for sent in sentences:
        # Count words in the sentence
        words = sent.split()
        word_counts.append(len(words))

    # Calculate the average
    return sum(word_counts) / len(sentences)

def character_ratio(s: str) -> Dict[str, float]:
    """Calculate the ratio of uppercase, lowercase, and numeric characters.

    Args:
        s: The input string to analyze

    Returns:
        Dictionary with ratios for 'uppercase', 'lowercase', and 'numeric'

    Example:
        >>> character_ratio("Hello123")
        {'uppercase': 0.125, 'lowercase': 0.5, 'numeric': 0.375}
    """
    if not s:
        return {'uppercase': 0.0, 'lowercase': 0.0, 'numeric': 0.0}

    # Count character types
    uppercase = sum(1 for c in s if c.isupper())
    lowercase = sum(1 for c in s if c.islower())
    numeric = sum(1 for c in s if c.isdigit())

    # Calculate ratios
    total_chars = len(s)
    return {
        'uppercase': uppercase / total_chars,
        'lowercase': lowercase / total_chars,
        'numeric': numeric / total_chars
    }

# ===== ML/NLP Preprocessing =====

def generate_ngrams(s: str, n: int = 2) -> List[str]:
    """Generate n-grams from the input string.

    Args:
        s: The input string
        n: Size of n-grams to generate (default: 2)

    Returns:
        List of n-grams

    Example:
        >>> generate_ngrams("hello", 2)
        ['he', 'el', 'll', 'lo']
    """
    # Convert to lowercase and split into words for word-level n-grams
    words = s.split()

    # For character-level n-grams if the input is a single word
    if len(words) == 1 and len(s) >= n:
        return [s[i:i+n] for i in range(len(s) - n + 1)]

    # For word-level n-grams
    if len(words) >= n:
        return [' '.join(words[i:i+n]) for i in range(len(words) - n + 1)]

    return []

def strip_accents(s: str) -> str:
    """Remove accents from characters (e.g., 'café' -> 'cafe').

    Args:
        s: The input string with accented characters

    Returns:
        String with accents removed

    Example:
        >>> strip_accents("café résumé")
        'cafe resume'
    """
    # Normalize to decomposed form (separate character and accent)
    nfkd_form = unicodedata.normalize('NFKD', s)
    # Remove all combining characters (accents)
    return ''.join([c for c in nfkd_form if not unicodedata.combining(c)])

def lemmatize_text(s: str) -> str:
    """Reduce words to their base form (lemma).

    This is a simple implementation that handles common English cases.
    For more advanced lemmatization, consider using NLTK or spaCy.

    Args:
        s: The input string

    Returns:
        String with words reduced to their base forms

    Example:
        >>> lemmatize_text("running cats and dogs")
        'run cat and dog'
    """
    # Special cases dictionary for common words
    special_cases = {
        "running": "run",
        "walking": "walk",
        "saying": "say",
        "going": "go",
        "doing": "do",
        "making": "make",
        "taking": "take",
        "coming": "come",
        "having": "have",
        "getting": "get",
        "putting": "put",
        "seeing": "see",
        "calling": "call",
        "trying": "try",
        "asking": "ask",
        "using": "use",
        "leaving": "leave",
        "talking": "talk",
    }

    # Simple lemmatization rules for common English cases
    lemma_rules = [
        # Order matters! More specific rules first
        (r'(\w+)ies\b', r'\1y'),       # flies -> fly
        (r'(\w+)es\b', r'\1'),         # boxes -> box
        (r'(\w+)s\b', r'\1'),          # cats -> cat
        (r'(\w+)ed\b', r'\1'),         # walked -> walk
        (r'(\w+)ing\b', r'\1e'),       # making -> make (for some verbs)
    ]

    # Process each word separately
    words = s.lower().split()
    result_words = []

    for word in words:
        # Check special cases first
        if word in special_cases:
            result_words.append(special_cases[word])
            continue

        # Apply rules in order
        for pattern, replacement in lemma_rules:
            if re.match(pattern, word):
                word = re.sub(pattern, replacement, word)
                break  # Stop after first match

        result_words.append(word)

    return ' '.join(result_words)

def is_ascii(s: str) -> bool:
    """Check if the string contains only ASCII characters.

    Args:
        s: The input string to check

    Returns:
        True if all characters are ASCII, False otherwise

    Example:
        >>> is_ascii("Hello World")
        True
        >>> is_ascii("café")
        False
    """
    # Try to encode as ASCII - if it works, all characters are ASCII
    try:
        s.encode('ascii')
        return True
    except UnicodeEncodeError:
        return False

# ===== Validation Functions =====

def is_valid_email(s: str) -> bool:
    """Validate if a string is a properly formatted email address.

    Args:
        s: The input string to validate

    Returns:
        True if the string is a valid email address, False otherwise

    Example:
        >>> is_valid_email("user@example.com")
        True
        >>> is_valid_email("invalid-email")
        False
    """
    # RFC 5322 compliant email regex pattern
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, s))

def is_valid_url(s: str) -> bool:
    """Validate if a string is a properly formatted URL.

    Args:
        s: The input string to validate

    Returns:
        True if the string is a valid URL, False otherwise

    Example:
        >>> is_valid_url("https://example.com")
        True
        >>> is_valid_url("not-a-url")
        False
    """
    # URL validation pattern
    pattern = r'^(https?|ftp)://[^\s/$.?#].[^\s]*$'
    return bool(re.match(pattern, s))

def is_valid_ip(s: str) -> bool:
    """Check if a string is a valid IP address (IPv4 or IPv6).

    Args:
        s: The input string to validate

    Returns:
        True if the string is a valid IP address, False otherwise

    Example:
        >>> is_valid_ip("192.168.1.1")
        True
        >>> is_valid_ip("2001:0db8:85a3:0000:0000:8a2e:0370:7334")
        True
        >>> is_valid_ip("not-an-ip")
        False
    """
    try:
        ipaddress.ip_address(s)
        return True
    except ValueError:
        return False

def is_valid_date(s: str, format: str = '%Y-%m-%d') -> bool:
    """Check if a string matches a date format.

    Args:
        s: The input string to validate
        format: The expected date format (default: '%Y-%m-%d')

    Returns:
        True if the string is a valid date in the specified format, False otherwise

    Example:
        >>> is_valid_date("2023-01-15")
        True
        >>> is_valid_date("01/15/2023", format="%m/%d/%Y")
        True
        >>> is_valid_date("not-a-date")
        False
    """
    try:
        datetime.datetime.strptime(s, format)
        return True
    except ValueError:
        return False

def contains_special_characters(s: str) -> bool:
    """Check if the string contains special characters.

    Args:
        s: The input string to check

    Returns:
        True if the string contains special characters, False otherwise

    Example:
        >>> contains_special_characters("Hello!")
        True
        >>> contains_special_characters("HelloWorld123")
        False
    """
    # Check for any character that is not alphanumeric or whitespace
    return bool(re.search(r'[^a-zA-Z0-9\s]', s))
