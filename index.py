import re

#Replacing words
def replace_word(input_text):

    # Replace 'harsh' with 'college'
    output_text = input_text.replace('harsh', 'college')
    
    # Return output
    return output_text


#Converting to lowercase
def convert_to_lowercase():

    # Read in input file
    with open("input3.txt", "r") as f:
        input_text = f.read()

    # Convert to lowercase
    output_text = input_text.lower()

    # Write output to file
    with open("output3.txt", "w") as f:
        f.write(output_text.rstrip())

    # Return output
    return output_text

# read in contents of input.txt
with open("harsh.txt", "r") as f:
    document = f.read()

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
