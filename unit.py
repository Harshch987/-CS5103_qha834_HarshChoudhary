import unittest
from index import replace_word, convert_to_lowercase, count_li, remove_special_chars,change_word, changed_word

class TestReplaceWords(unittest.TestCase):

    def test_replace_words(self):
        with open("harsh.txt", "r") as f:
            input_text = f.read()
        output_text = replace_word(input_text)

        with open("output.txt", "w") as f:
            f.write(output_text)
        with open("expected_output.txt", "r") as f:
            expected_output = f.read().strip()

    def test_count_lowercase(self):
        with open("harsh.txt", "r") as f:
            input_text = f.read()
            num_lowercase = sum(1 for char in input_text if char.islower())
        self.assertEqual(num_lowercase, 24)

    def test_convert_to_lowercase(self):
        input_file = "input3.txt"
        expected_output = "i am in harsh studying in utsa"
        output_text = convert_to_lowercase()
        self.assertEqual(output_text, expected_output)
        with open("output3.txt", "r") as f:
            output_file_contents = f.read()
        self.assertEqual(output_text, expected_output)

    def test_count_li(self):
        text = "Life is\nlike\nriding bicycle"
        expected_num_lines = 3
        expected_num_chars = 23
        actual_num_lines, actual_num_chars = count_li(text)
        self.assertEqual(expected_num_lines, actual_num_lines)
        self.assertEqual(expected_num_chars, actual_num_chars)
    
    def test_count_li_empty(self):
        text = ""
        expected_num_lines = 0
        expected_num_chars = 0
        actual_num_lines, actual_num_chars = count_li(text)
        self.assertEqual(expected_num_lines, actual_num_lines)
        self.assertEqual(expected_num_chars, actual_num_chars)

    def test_removes_special_chars(self):
        self.assertEqual(remove_special_chars("Hello, world!"), "Hello world")
        self.assertEqual(remove_special_chars("This is awesome."), "This is awesome")
        self.assertEqual(remove_special_chars("I am good!"), "I am good")
    
    def test_multi_occurrences(self):
        original_text = "the quick brown fox jumps over the lazy dog"
        pattern = "the"
        replacement = "a"
        expected_output = "a quick brown fox jumps over a lazy dog"
        actual_output = change_word(original_text, pattern, replacement)
        self.assertEqual(actual_output, expected_output)    
    
    def test_replace_word_with_symbol(self):
        original_text = "The quick-brown fox jumps over the lazy dog"
        pattern = "quick-brown"
        replacement = "slow"
        expected_output = "The slow fox jumps over the lazy dog"
        actual_output = change_word(original_text, pattern, replacement)
        self.assertEqual(actual_output, expected_output)
    
    def test_pattern_not_found(self):
        original_text = "The quick brown fox jumps over the lazy dog"
        pattern = "cat"
        replacement = "dog"
        expected_output = "Pattern not found in text."
        actual_output = changed_word(original_text, pattern, replacement)
        self.assertEqual(actual_output, expected_output)



if __name__ == '__main__':
    unittest.main()
