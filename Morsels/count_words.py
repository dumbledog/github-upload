"""
I want you to write a function that accepts a string and returns a mapping (a dictionary or dictionary-like structure) that has words as the keys and the number of times each word was seen as the values.

Your function should work like this:

>>> count_words("oh what a day what a lovely day")
{'oh': 1, 'what': 2, 'a': 2, 'day': 2, 'lovely': 1}
>>> count_words("don't stop believing")
{"don't": 1, 'stop': 1, 'believing': 1}

Bonus 1

As a bonus, make sure your function works well with mixed case words:

>>> count_words("Oh what a day what a lovely day")
{'oh': 1, 'what': 2, 'a': 2, 'day': 2, 'lovely': 1}
Bonus 2

For even more of a bonus try to get your function to ignore punctuation outside of words:

>>> count_words("Oh what a day, what a lovely day!")
{'oh': 1, 'what': 2, 'a': 2, 'day': 2, 'lovely': 1}
"""

from collections import Counter
import string


def count_words(s):
    input = s.split(' ')
    input = [word.lower() for word in input]
    # input = [
    #     [
    #         letter
    #         for letter in word
    #         if letter in string.ascii_letters
    #     ]
    #     for word in s.split(' ')
    # ]
    words = Counter(input)

    return dict(words)


