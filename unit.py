import unittest
from index import replace_word, convert_to_lowercase

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

if __name__ == '__main__':
    unittest.main()