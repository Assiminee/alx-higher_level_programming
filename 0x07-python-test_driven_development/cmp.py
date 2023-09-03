#!/usr/bin/python3
import difflib
 
with open('tt') as file_1:
    file_1_text = file_1.readlines()
 
with open('ttcmp') as file_2:
    file_2_text = file_2.readlines()
 
# Find and print the diff:
for line in difflib.unified_diff(
        file_1_text, file_2_text, fromfile='tt',
        tofile='ttcmp', lineterm=''):
    print(line)
