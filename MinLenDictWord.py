



import sys

from math import  *


char_set = ['b','c','d','e']
dict = ['a','b','c','d','ab','ba','bc','bd','asfs', 'bcef','abcd','bcel','bcde']


def findindex_forminlen(min_len):
    global  dict
    if min_len < 1:
        return -1
    min_len_index = -1
    for i in xrange(0,len(dict)-1):
        if (len(dict[i]) >= min_len):
            min_len_index = i
            break
    return min_len_index


def search_chars_in_word(word):
    global  char_set
    print ("checking word: " + str(word))
    if word == None:
        return False
    num_chars_in_set = len(char_set)
    for x in char_set:
        if x not in word:
            return False
    return True

def find_min_len_matching_word():
    global char_set
    global dict

    if char_set == None or dict == None:
        return "Invalid parameters"
    min_len_start_index = findindex_forminlen(len(char_set))

    if min_len_start_index == -1:
        return False
    for i in xrange(min_len_start_index,len(dict)):
        word = dict[i]
        ret = search_chars_in_word(word)

        if ret:
            return word
        else:
            continue

    return "No match"


if __name__ == '__main__':
    print (str(find_min_len_matching_word()))
