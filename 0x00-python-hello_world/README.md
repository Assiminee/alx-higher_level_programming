
# 0x00. Python - Hello, World

For this project, we expect you to look at this concept:
+ Python Programming:
	+ [The Python Tutorial](https://docs.python.org/3.4/tutorial/index.html)
	+ [Python Programming: An Introduction to Computer Science 3rd edition](https://nibmehub.com/opac-service/pdf/read/Python%20Programming%20_%20an%20introduction%20to%20computer%20science-%203rd%20Edition.pdf)
	+ [Derek Banas’ Learn to program](https://www.youtube.com/playlist?list=PLGLfVvz_LVvTn3cK5e6LjhgGiSeVlIRwt)
	+ [The Python Guru](https://thepythonguru.com/)
	+ [New string formatting](https://pyformat.info/)
	+ [Garbage collector](https://thp.io/2012/python-gc/python_gc_final_2012-01-22.pdf)
	+ [Python Interpreter](https://aosabook.org/en/500L/a-python-interpreter-written-in-python.html)
	+ [Python bytecode](https://docs.python.org/3.4/library/dis.html)

## Resources
### Read or watch
+ [How To Use String Formatters in Python 3](https://realpython.com/python-f-strings/)
+ [Pycodestyle – Style Guide for Python Code](https://pypi.org/project/pycodestyle/)

## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

### General
+ Why Python programming is awesome
+ Who created Python
+ Who is Guido van Rossum
+ Where does the name ‘Python’ come from
+ What is the Zen of Python
+ How to use the Python interpreter
+ How to print text and variables using print
+ How to use strings
+ What are indexing and slicing in Python
+ What is the official Python coding style and how to check your code with pycodestyle

## Requirements
### Python Scripts
+ Allowed editors: vi, vim, emacs
+ All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
+ All your files should end with a new line
+ The first line of all your files should be exactly #!/usr/bin/python3
+ A README.md file at the root of the repo, containing a description of the repository
+ A README.md file, at the root of the folder of this project, is mandatory
+ Your code should use the pycodestyle (version 2.8.*)
+ All your files must be executable
+ The length of your files will be tested using wc
## Shell Scripts
+ Allowed editors: vi, vim, emacs
+ All your scripts will be tested on Ubuntu 20.04 LTS
+ All your scripts should be exactly two lines long (wc -l file should print 2)
+ All your files should end with a new line
+ The first line of all your files should be exactly #!/bin/bash
+ All your files must be executable
## C Scripts
+ Allowed editors: vi, vim, emacs
+ All your files will be compiled on Ubuntu 20.04 LTS using gcc, using the options -Wall -Werror -Wextra -pedantic -std=gnu89
+ All your files should end with a new line
+ Your code should use the Betty style. It will be checked using betty-style.pl and betty-doc.pl
+ You are not allowed to use global variables
+ No more than 5 functions per file
+ In the following examples, the main.c files are shown as examples. You can use them to test your functions, but you don’t have to push them to your repo (if you do we won’t take them into account). We will use our own main.c files at compilation. Our main.c files might be different from the one shown in the examples
+ The prototypes of all your functions should be included in your header file called lists.h
+ Don’t forget to push your header file
+ All your header files should be include guarded

# Tasks
## [0-run](https://github.com/Assiminee/alx-higher_level_programming/blob/master/0x00-python-hello_world/0-run)

Write a Shell script that runs a Python script.

The Python file name will be saved in the environment variable $PYFILE

## [1-run_inline](https://github.com/Assiminee/alx-higher_level_programming/blob/master/0x00-python-hello_world/1-run_inline)

Write a Shell script that runs Python code.

The Python code will be saved in the environment variable $PYCODE

## [2-print.py](https://github.com/Assiminee/alx-higher_level_programming/blob/master/0x00-python-hello_world/2-print.py)

Write a Python script that prints exactly "Programming is like building a multilingual puzzle, followed by a new line.

+ Use the function print

## [3-print_number.py](https://github.com/Assiminee/alx-higher_level_programming/blob/master/0x00-python-hello_world/3-print_number.py)

Complete this [source code](https://github.com/alx-tools/0x00.py/blob/master/3-print_number.py) in order to print the integer stored in the variable number, followed by Battery street, followed by a new line.

+ You can find the source code [here](https://github.com/alx-tools/0x00.py/blob/master/3-print_number.py)
+ The output of the script should be:
    + the number, followed by Battery street,
    + followed by a new line
+ You are not allowed to cast the variable number into a string
+ Your code must be 3 lines long
+ You have to use f-strings tips

## [4-print_float.py](https://github.com/Assiminee/alx-higher_level_programming/blob/master/0x00-python-hello_world/4-print_float.py)

Complete the source code in order to print the float stored in the variable number with a precision of 2 digits.

+ You can find the source code [here](https://github.com/alx-tools/0x00.py/blob/master/4-print_float.py)
+ The output of the program should be:
    + Float:, followed by the float with only 2 digits
    + followed by a new line
+ You are not allowed to cast number to string
+ You have to use f-strings

## [5-print_string.py](https://github.com/Assiminee/alx-higher_level_programming/blob/master/0x00-python-hello_world/5-print_string.py)

Complete this source code in order to print 3 times a string stored in the variable str, followed by its first 9 characters.

+ You can find the source code [here](https://github.com/alx-tools/0x00.py/blob/master/5-print_string.py)
+ The output of the program should be:
    + 3 times the value of str
    + followed by a new line
    + followed by the 9 first characters of str
    + followed by a new line
+ You are not allowed to use any loops or conditional statement
+ Your program should be maximum 5 lines long

## [6-concat.py](https://github.com/Assiminee/alx-higher_level_programming/blob/master/0x00-python-hello_world/6-concat.py)

Complete this source code to print Welcome to Holberton School!

+ You can find the source code [here](https://github.com/alx-tools/0x00.py/blob/master/6-concat.py)
+ You are not allowed to use any loops or conditional statements.
+ You have to use the variables str1 and str2 in your new line of code
+ Your program should be exactly 5 lines long

## [7-edges.py](https://github.com/Assiminee/alx-higher_level_programming/blob/master/0x00-python-hello_world/7-edges.py)

Complete this source code

+ You can find the source code [here](https://github.com/alx-tools/0x00.py/blob/master/7-edges.py)
+ You are not allowed to use any loops or conditional statements
+ Your program should be exactly 8 lines long
+ word_first_3 should contain the first 3 letters of the variable word
+ word_last_2 should contain the last 2 letters of the variable word
+ middle_word should contain the value of the variable word without the first and last letters

## [8-concat_edges.py](https://github.com/Assiminee/alx-higher_level_programming/blob/master/0x00-python-hello_world/8-concat_edges.py)

Complete this source code to print object-oriented programming with Python, followed by a new line.

+ You can find the source code [here](https://github.com/alx-tools/0x00.py/blob/master/8-concat_edges.py)
+ You are not allowed to use any loops or conditional statements
+ Your program should be exactly 5 lines long
+ You are not allowed to create new variables
+ You are not allowed to use string literals

## [9-easter_egg.py](https://github.com/Assiminee/alx-higher_level_programming/blob/master/0x00-python-hello_world/9-easter_egg.py)

Write a Python script that prints “The Zen of Python”, by TimPeters, followed by a new line.

+ Your script should be maximum 98 characters long (please check with wc -m 9-easter_egg.py)

## [10-check_cycle.c](https://github.com/Assiminee/alx-higher_level_programming/blob/master/0x00-python-hello_world/10-check_cycle.c)

Technical interview preparation:

+ You are not allowed to google anything
+ Whiteboard first
+ This task and all future technical interview prep tasks will include checks for the efficiency of your solution, i.e. is your solution’s runtime fast enough, does your solution require extra memory usage / mallocs, etc.
Write a function in C that checks if a singly linked list has a cycle in it.

+ Prototype: int check_cycle(listint_t *list);
+ Return: 0 if there is no cycle, 1 if there is a cycle
Requirements:

+ Only these functions are allowed: write, printf, putchar, puts, malloc, free
[lists.h](https://github.com/Assiminee/alx-higher_level_programming/blob/master/0x00-python-hello_world/lists.h)
[10-linked_lists.c](https://github.com/Assiminee/alx-higher_level_programming/blob/master/0x00-python-hello_world/10-linked_lists.c)
[10-main.c](https://github.com/Assiminee/alx-higher_level_programming/blob/master/0x00-python-hello_world/10-main.c)

## [100-write.py](https://github.com/Assiminee/alx-higher_level_programming/blob/master/0x00-python-hello_world/100-write.py)

Write a Python script that prints exactly and that piece of art is useful - Dora Korpar, 2015-10-19, followed by a new line.

+ Use the function write from the sys module
+ You are not allowed to use print
+ Your script should print to stderr
+ Your script should exit with the status code 1

## [101-compile](https://github.com/Assiminee/alx-higher_level_programming/blob/master/0x00-python-hello_world/101-compile)

Write a script that compiles a Python script file.

The Python file name will be stored in the environment variable $PYFILE

The output filename has to be $PYFILEc (ex: export PYFILE=my_main.py => output filename: my_main.pyc)

## [102-magic_calculation.py](https://github.com/Assiminee/alx-higher_level_programming/blob/master/0x00-python-hello_world/102-magic_calculation.py)

Write the Python function def magic_calculation(a, b): that does exactly the same as the following Python bytecode:

```
 3            0 LOAD_CONST              1 (98)
             3 LOAD_FAST               0 (a)
             6 LOAD_FAST               1 (b)
             9 BINARY_POWER
             10 BINARY_ADD
             11 RETURN_VALUE
```
