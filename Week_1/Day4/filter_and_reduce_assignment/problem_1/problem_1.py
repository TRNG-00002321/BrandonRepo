"""
1. Filter Strings by Length
Given a list of strings, use filter() to create a new list containing only the
strings with a length greater than 5.
Example
words = ["apple", "banana", "cat", "dog", "elephant", "frog"]
"""


words = ["apple", "banana", "cat", "dog", "elephant", "frog"]

new_words = list(filter(lambda x: len(x) > 5, words))

print(new_words)