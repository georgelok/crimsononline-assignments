"""
Question 1

objectives
    - get more comfortable with Python
    - learn how to handle exceptions
    - work with the file system
"""
from collections import Counter
import re
import string

def common_words(filename):
    """question 1a

    Write a function that takes a path to a text file as input. The function
    should open the file, count the number of occurrences of each word, and
    return a sorted list of the most common words.
    """

    """" We return the top 10 most common words.
    """
    textfile = open(filename, 'r')
    word_list=re.split('\s+',file(filename).read().lower())
    for word in word_list : 
        for char in string.punctuation : 
            word = word.replace(char, '')
    common_words = []
    for key,value in Counter(word_list).most_common(10) :
        common_words.append(key)
    textfile.close()
    return common_words

def common_words_min(filename, min_chars):
    """question 1b

    Modify this function to take a second argument that specifies the
    minimum number of characters long a word can be to be counted.
    """
    """" We return the top 10 most common words.
    """
    textfile = open(filename, 'r')
    temp_list=re.split('\s+',file(filename).read().lower())
    for word in temp_list : 
        for char in string.punctuation : 
            word = word.replace(char, '')
    word_list = [s for s in temp_list if len(s) >= min_chars]
    common_words = []
    for key,value in Counter(word_list).most_common(10) :
        common_words.append(key)
    textfile.close()
    return common_words

def common_words_tuple(filename, min_chars):
    """question 1c

    Modify this function to return a list of tuples rather than just a list
    of strings. Each tuple should be of the format
        (word, number of occurrences)
    Of course, the list of tuples should still be sorted as in part a.
    """
    textfile = open(filename, 'r')
    temp_list=re.split('\s+',file(filename).read().lower())
    for word in temp_list : 
        for char in string.punctuation : 
            word = word.replace(char, '')
    word_list = [s for s in temp_list if len(s) >= min_chars]
    textfile.close()
    return Counter(word_list).most_common(10)

def common_words_safe(filename, min_chars):
    """question 1d

    Modify your function so that it catches the IOError exception and prints
    a friendly error message.
    """
    try :
        textfile = open(filename, 'r')
    except IOError:
        print 'File missing!'
        return
    temp_list=re.split('\s+',file(filename).read().lower())
    for word in temp_list : 
        for char in string.punctuation : 
            word = word.replace(char, '')
    word_list = [s for s in temp_list if len(s) >= min_chars]
    textfile.close()
    return Counter(word_list).most_common(10)