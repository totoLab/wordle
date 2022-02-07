import re
import sys
import os

def match_length(input_list, pattern, delete_newline):
    words = []
    for line in input_list:
        if delete_newline:
            line = line[:len(line)-1]
        match_obj = re.search(pattern, line) 
        if match_obj:
            line = line.lower()
            words.append(line)

    return words

def every_char_line(chars, line):
    for char in chars:
        if char in line:
            return False
    return True


def match_chars(input_list, chars):
    words = []
    for line in input_list:
        line = line.lower()
        if every_char_line(chars, line):
            words.append(line)

    return words

regex = '^.{5}$' # only five letter words

raw_file = input("Input file name: ")
path =  os.path.dirname(os.path.realpath(__file__))
my_file = path + "/" + raw_file

with open(my_file, "r") as f:
    final_list = match_length(f, regex, True)

dontwant = ["'", "ò", "à", "ì", "è", "é", "ù"]
clipboard = match_chars(final_list, dontwant)

for word in clipboard:
    print(word)