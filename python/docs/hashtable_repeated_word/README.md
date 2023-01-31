# Hashtable Repeated Word 
Practice in using hashtables and their effiency for looking up a key value pair. 
## Challenge
Write a function called repeated word that finds the first word to occur more than once in a string
- Arguments: string
- Return: string


## Approach & Efficiency
Because we have to iterate through our list that stores our split up text, time and space complexity of that is O(n). When it comes to checking if a word has already been seen, time and space complexity are O(1). This is because we are using a hash table to set a new word and also to check (has) if the word exists in our hash table.

## Whiteboard
![](hash_repeat_word.jpg)

## Solution

Our function takes in a string and returns the first repeated word. In order to iterate through the string we need to split the string into individual words. At the same time we need to remove any punctuation and set our words to lower. This is done with list comprehension storing the words in a list. For speedy lookup we instantiate a hashtable. We begin to iterate through our words list, if a word is not in our hastable it added. If a word exists in our hashtable, the word returned. This returns the first repeadted word and halts any other lookup.

[Solution](https://github.com/mramirez92/data-structures-and-algorithms/blob/main/python/code_challenges/hashtable_repeated_word.py)

## Links and Resources
[Remove Punctuation](https://datagy.io/python-remove-punctuation-from-string/)

[.translate()](https://docs.python.org/3/library/stdtypes.html?highlight=translate#str.translate)

