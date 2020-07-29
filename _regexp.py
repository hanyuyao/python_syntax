'''
A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.
RegEx can be used to check if a string contains the specified search pattern.
'''

import re

txt = 'Hi, my name is Allen, and I am 21 years old.'
x = re.findall("[A-Z0-9]",txt)
print(x)                    # ['H', 'A', 'I', '2', '1']

x = re.findall('.', txt)
print(x)
print("----------------------------------------------")

# /[0-9]/ == /\d/
# /[a-zA-Z0-9_]/ == /\w/
# /./ : any character except newline character
# ^ : start with, $ : end with
# {} : specify number of occurences
# * : zero or more occurences, ex:/al*/ -> al, all, alll...
# + : one or more occurences, ex:/al+/ -> all, alll, allll...

# check if it is legal cellphone number
phone_num = ['0972881476', '1542369874', '09321112223', '09**11']
for x in phone_num:
    print(re.search("^09\d{8}$", x))