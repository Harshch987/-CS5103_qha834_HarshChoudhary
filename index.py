"""
Second requirement change
"""
import re
def change_word(text, pattern, replacement):
    """
    It replaces the words.
    """
    # Split the text into a list of words
    words = re.split(r" |\t", text)

    # Loop through each word and replace if it matches the pattern
    for i in range(len(words)):
        if words[i] == pattern and (i == 0 or not words[i-1].endswith("\t")):
            words[i] = replacement

    # Join the words back into a single string
    changed_text = ' '.join(words)

    return changed_text
original_text = "ab cd ef"
pattern = "ab"
replacement = "cd"
changed_text = change_word(original_text, pattern, replacement)
print(f"Final Result: {changed_text}")
#Replacing words
def replace_word(input_text):
    """
    It replaces the word
    """

    # Replace 'harsh' with 'college'
    output_text = input_text.replace('harsh', 'college')
    # Return output
    return output_text

with open("inp.txt", "r", encoding="utf-8") as file:
    text = file.read()

# Count the number of lines in the text
line_count = len(text.split('\n'))
print(f"Number of lines: {line_count}")
# Count the number of characters in the text
char_count = len(text)
print(f"Number of characters: {char_count}")

def changed_word(text, pattern, replacement):
    if pattern in text:
        words = text.split()
        new_words = []
        for word in words:
            if word == pattern:
                new_words.append(replacement)
            else:
                new_words.append(word)
        return " ".join(new_words)
    else:
        return "Pattern not found in text."


def count_li(text):
    """
    It counts number of lines and characters
    """
    num_lines = len(text.splitlines())
    num_chars = len(''.join(text.split()))
    return num_lines, num_chars


def remove_special_chars(string):
    """
    It removes special character.
    """
    special_chars = "!@#$%^&*()_+{}:\"<>?\|[];',./`~"
    return "".join([char for char in string if char not in special_chars])



#Converting to lowercase
def convert_to_lowercase():
    """
    It converts into lowercase
    """

    # Read in input file
    with open("input3.txt", "r", encoding="utf-8") as file:
        input_text = file.read()

    # Convert to lowercase
    output_text = input_text.lower()

    # Write output to file
    with open("output3.txt", "w", encoding="utf-8") as file:
        file.write(output_text.rstrip())

    # Return output
    return output_text

# read in contents of input.txt
with open("harsh.txt", "r", encoding="utf-8") as file:
    document = file.read()

# replace all non-alphanumeric characters with whitespace
document = re.sub(r"[^\w\s]", " ", document)

# split document into list of words using whitespace as separator
texts = re.split(r"\s+", document)

# count frequency of each unique word
word_counts = {}
for some in texts:
    if some not in word_counts:
        word_counts[some] = 0
    word_counts[some] += 1

# print results
for word, count in word_counts.items():
    print(word, count)
