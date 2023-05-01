#CS5103 Software Engineering : Course Project   Professor: Xiaoyin Wang
-----------------------------------------------------------------------
Name-Harsh Choudhary, qha834  
Checkpoint: 3/10/2023  
Language:Python3

**Second Requirement Change**  
Word Statistics: The second requirement change is to allow replacement of all occurrences of a given word to a given replacement word. Note that the replacement happens only when the given pattern word matches with a whole word. For example, for text “ab cd ef”, replace “a” with “b” will result in no change, while replace “ab” with “cd” will result in “cd cd ef”.



**TEST CASE 1 - Word Match Replacement**

1.Enter a string or text into the python program.  
2.The program does not replace the word if pattern doesn't matches with the original text.  
3.It shouldnot be able to replace because pattern must match with the original text for replacement to happen.  

Input: Hello world python


Pattern: Dog

Replacement: Cat
       

Output: Hello world python



**TEST CASE 2 - String and Symbol Replacement**

1.Enter a string or text into the python program.  
2.The program replaces the word if any word in original text is combination of string and symbols.  
3.It only replaces that specific word which is the combination of string and symbols.  

Input: H@llo world python


Pattern: H@llo

Replacement: Hello
       

Output: Hello world python



**TEST CASE 3 - Multi Occurence Word Replacement**

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
 

------------------------------------------------------------------
Your code has been rated at 9.14/10 (previous run: 8.57/10, +0.57)  

Ran 9 tests in 0.002s  

OK


Code detection using pylint:
----------------------------

<img width="664" alt="Screenshot 2023-04-30 at 7 00 14 PM" src="https://user-images.githubusercontent.com/54935713/235382195-f9d1125a-c14c-4833-b0d0-313aba73d725.png">






#How to run program On Terminal 
-------------------------------------------

Install Python3 before starting.  
Change directory to where 'index.py' is located.   
Enter 'python3 index.py' on terminal to run python file.  
The program will execute and will print the output accordingly to the text taken as input.   
It prints the the count of unique words, number of lines and number of characters.  

Followed by all unit test which performs operations of string as :
1. Word replacement.
2. Count lowercase characters.  
3. Convert all uppercase character to lowercase.  
4. Returns the count of each character and lines.  
5. Checks for input text is empty string.  
6. Removes all the special characters.  
7. Replace the word only if pattern match original text (new).  
8. Replace the word which match string and symbol (new).  
9. Multi Occurence Word Replacement (new).



