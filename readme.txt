CS5103 Software Engineering : Course Project   Professor: Xiaoyin Wang

Name-Harsh Choudhary, qha834
Checkpoint: 3/10/2023
Language:Python3

Second Requirement Change

TEST CASE 1:

1.Enter a string or text into the python program.
2.The program doesnot replace the word if pattern doesn't matches with the original text.
3.It shouldnot be able to replace because pattern must match with the original text for replacement to happen.

Input: Hello world python


Pattern: Dog

Replacement: Cat
       

Output: Hello world python



TEST CASE 2:

1.Enter a string or text into the python program.
2.The program replaces the word if any word in original text is combination of string and symbols.
3.It only replaces that specific word which is the combination of string and symbols.

Input: H@llo world python


Pattern: H@llo

Replacement: Hello
       

Output: Hello world python



TEST CASE 3:

1.Enter a string or text into the python program.
2.The program replace the word even there are multi occurrence word in the original text. 
3.It should be able to replace multiple exact words at the same time.

Input: Hello world python world


Pattern: world

Replacement: universe
       

Output: Hello universe python universe

Test case output:





First Requirement Change

TEST CASE 1 -

1.Enter a string or text into the python program.
2.The program returns the count of each character and count of lines present in the string.
3.It should be able to read across spaces, tabs, and newline character as seperators.

Input: Hello 
       World 
       Python Program

Output: Lines: 3, Characters: 23

TEST CASE 2 -

1.Enter a string or text into the python program.
2.The program checks whether the input text is empty string and returns ouput accordingly.

Input: 

Output: Lines: 0, Characters: 0
TEST CASE 3 -

1.Enter a string or text into the python program.
2.The program removes all the special characters present in the input string.
3.It should be able to read across spaces, tabs, and newline character as seperators.

Input: Hello, world!

Output: Hello world

Initial Test Case

Program to count the frequency of each unique word with 3 unit tests.
(supports combinations of space, tab, and newline characters as separators).

TEST CASE 1 -

1.Enter a string or text into the python program.  
2.The program replaces the word in the string with the new word and returns output.

Input: Hello World Python Program

Output: Hello World Java Program

TEST CASE 2-

1.Enter a string or text into the python program.  
2.The program returns the count frequencey of all lowercase character as output.  
3.It should be able to read spaces, tabs, and newline characters as separators.  
4.Print all characters count present in string.  

Input: Hello World Python Program

Output: 19

TEST CASE 3

1.Enter a string or text into the python program.  
2.The program converts all uppercase characters to lowercase and prints the output.

Input: Hello World Python Program

Output: hello world python program

How to run program On Terminal 

Install Python3 before starting.
Change directory to where 'index.py' is located. 
Enter 'python3 index.py' on terminal to run python file.
The program will execute and will print the output accordingly to the text taken as input. 
It prints the the count of unique words.

Followed by 3 unit test which performs operations of string as 
1. Word replacement.
2. Count lowercase characters.
3. Convert all uppercase character to lowercase.
