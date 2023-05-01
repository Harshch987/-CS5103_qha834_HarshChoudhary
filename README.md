#CS5103 Software Engineering : Course Project   Professor: Xiaoyin Wang
-----------------------------------------------------------------------
Name-Harsh Choudhary, qha834  
Checkpoint: 3/10/2023  
Language:Python3

Second Requirement Change:
Word Statistics: The second requirement change is to allow replacement of all occurrences of a given word to a given replacement word. Note that the replacement happens only when the given pattern word matches with a whole word. For example, for text “ab cd ef”, replace “a” with “b” will result in no change, while replace “ab” with “cd” will result in “cd cd ef”.



TEST CASE 1 

1.Enter a string or text into the python program.
2.The program doesnot replace the word if pattern doesn't matches with the original text.
3.It shouldnot be able to replace because pattern must match with the original text for replacement to happen.

Input: Hello world python


Pattern: Dog

Replacement: Cat
       

Output: Hello world python



TEST CASE 2 

1.Enter a string or text into the python program.
2.The program replaces the word if any word in original text is combination of string and symbols.
3.It only replaces that specific word which is the combination of string and symbols.

Input: H@llo world python


Pattern: H@llo

Replacement: Hello
       

Output: Hello world python



TEST CASE 3 

1.Enter a string or text into the python program.
2.The program replace the word even there are multi occurrence word in the original text. 
3.It should be able to replace multiple exact words at the same time.

Input: Hello world python world


Pattern: world

Replacement: universe
       

Output: Hello universe python universe


Test Case Output:
-----------------
......
----------------------------------------------------------------------
Ran 9 tests in 0.002s

OK

Code detection using pylint:
----------------------------

<img width="664" alt="Screenshot 2023-04-30 at 7 00 14 PM" src="https://user-images.githubusercontent.com/54935713/235382195-f9d1125a-c14c-4833-b0d0-313aba73d725.png">








Program to count the frequency of each unique word.

First Requirement Change:-
Addition of two feature to count the number of lines and characters with 3 unit tests.
(supports combinations of space, tab, and newline characters as separators).

TEST CASE 1 -

1.Enter a string or text into the python program.  
2.The program returns the count of each character and count of lines present in the string.  
3.It should be able to read across spaces, tabs, and newline character as seperators.

Input: Hello \nWorld \nPython Program  
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

#How to run program On Terminal 
-------------------------------------------

Install Python3 before starting.  
Change directory to where 'index.py' is located.   
Enter 'python3 index.py' on terminal to run python file.  
The program will execute and will print the output accordingly to the text taken as input.   
It prints the the count of unique words, number of lines and number of characters.  

Followed by unit test which performs operations of string as :
1. Word replacement.
2. Count lowercase characters.
3. Convert all uppercase character to lowercase.
4. Returns the count of each character and lines (new).
5. Checks for input text is empty string (new).
6. Removes all the special characters (new).


