import unittest
from funstrings.operations import (
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

class TestFunStringsOperations(unittest.TestCase):

    def test_reverse_string(self):
        self.assertEqual(reverse_string("Hello"), "olleH")
        self.assertEqual(reverse_string(""), "")

    def test_count_vowels(self):
        self.assertEqual(count_vowels("Hello World"), 3)
        self.assertEqual(count_vowels(""), 0)

    def test_count_consonants(self):
        self.assertEqual(count_consonants("Hello World"), 7)
        self.assertEqual(count_consonants("aeiou"), 0)

    def test_is_palindrome(self):
        self.assertTrue(is_palindrome("Madam"))
        self.assertTrue(is_palindrome("A man, a plan, a canal, Panama"))
        self.assertFalse(is_palindrome("Hello"))

    def test_to_upper(self):
        self.assertEqual(to_upper("hello"), "HELLO")

    def test_to_lower(self):
        self.assertEqual(to_lower("HELLO"), "hello")

    def test_word_count(self):
        self.assertEqual(word_count("Hello World"), 2)
        self.assertEqual(word_count("One"), 1)

    def test_sort_characters(self):
        self.assertEqual(sort_characters("cba"), "abc")
        self.assertEqual(sort_characters("cba", reverse=True), "cba")

    def test_remove_whitespace(self):
        self.assertEqual(remove_whitespace(" H e l l o "), "Hello")
        self.assertEqual(remove_whitespace(""), "")

if __name__ == "__main__":
    unittest.main()
