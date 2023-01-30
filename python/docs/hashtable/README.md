# Hashtables
Hash tables allow us to access data quickly by using key value pairs. 

## Challenge
Implement a Hashtable Class with the following methods:

`set` 
 - Arguments: key, value
 - Returns: nothing

`get`
- Arguments: key
- Returns: Value associated with that key in the table

`has`
- Arguments: key
- Returns: Boolean, indicating if the key exists in the table already.

`keys`
- Returns: Collection of keys

`hash`
- Arguments: key
- Returns: Index in the collection for that key

## Approach & Efficiency
Time complexity for this is O(1). Because we are assigning unique values to each key, we can find them directly without the needing to traverse all of our table. 
