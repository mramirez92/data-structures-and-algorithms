# Stacks and Queues Bracket

This [function](https://github.com/mramirez92/data-structures-and-algorithms/blob/main/python/code_challenges/stack_queue_brackets.py) takes in a string and returns a boolean. If the string contains closing and matching pairs, it returns True. If a pair of brackets is not complete it returns False.
![](brackets.jpg)

## Challenge
Write a function called validate brackets
Arguments: string
Return: boolean
representing whether or not the brackets in the string are balanced
There are 3 types of brackets:

Round Brackets : ()
Square Brackets : []
Curly Brackets : {}


## Approach & Efficiency
Function runs at O(n) since we are iterating through a string and pushing opening brackets into a temporary stack to use for comparing bracket pairs. Temp stack will increase in size depending on the amount of opening brackets we have in our string.
