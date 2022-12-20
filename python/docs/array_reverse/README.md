# Reverse an Array
<!-- Description of the challenge -->
Write a function called reverseArray which takes an list as an argument. Without utilizing any of the built-in methods, return list with elements in reversed order.

## Whiteboard Process

![Whiteboard](/array_reverse.jpg)


## Approach & Efficiency
<!-- What approach did you take? Discuss Why. What is the Big O space/time for this approach? -->
I used index of my list elements to slice and return the list in reverse order starting at -1. The returned list will increase in size (O(n)) as the function iterates through the entirety of the list. The function will run until it reaches the end of the list (O(1)).
