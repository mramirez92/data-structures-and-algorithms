# Stacks and Queues Brackets 

## Challenge
Write a function called validate brackets
Arguments: string
Return: boolean
representing whether or not the brackets in the string are balanced
There are 3 types of brackets:

Round Brackets : ()
Square Brackets : []
Curly Brackets : {}

## Whiteboard Process 
![whiteboard](brackets.jpg)
## Approach & Efficiency
Function runs in Big O(n), since we have to traverse our string and move the opening brackets to a temporaty holding stack. If our string is full of opening brackets, the temp stack will grow. 
## Solution:

[Solution](https://github.com/mramirez92/data-structures-and-algorithms/blob/main/python/code_challenges/stack_queue_brackets.py)
```
multi_bracket_validation("{([])}")
True
```

