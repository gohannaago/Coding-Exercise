# Coding Exercise
## Description 
Coding practice and interview prep in Python and C++

Problems from the website [Leetcode](https://leetcode.com)

since 12.01.2021

<br>

## Notes

- **Single / Double linked lists**: in Python this can be done by creating a LinkedList class and treating each list as objects (OOP), in c++ this can be done by using pointers. Done in [*2. Add two numbers*.](add_two_num.py)
- **float('inf')** (Python): this acts as an unbounded upper value for comparison, used in [*4. Median of two sorted arrays*.](mediantwosorted.py) 
- Time complexity for 'a in b' checks: doing *list a **in** list b* has time complexity in O(n) while using **dict** or **set** (**map** in c++) have time complexity O(nlogn). *implemented in [Three Sum](threesum.py)*
- **Unsigned Integers vs Signed Integers** : for 32bit integers, unsigned range from $0$ to $2^{32}$ while signed are $-2^{31}$ to $2^{31}$ *in [Number of Bits](numberofbits.py)* and [*190. Reverse Bits*](reverse_bits.py)
- **Depth First Search Algorithm (DFS)**: Algorithm for searching tree or graph datastructures 
    - recursively done by marking adjacent vertices, given an initial vertex
    - Time complexity : O(V+E), V being number of vertices and E number of edges
    - Space complexity: O(V) 

    implemented in [*200. Number of Islands*](number_of_islands.py).
- **Comparing Strings**: 
    - ***is*** is used for *identity comparison* : if the strings are saved in same memory location
    - **==** is used for *equality comparison* : if the strings contain the same characters
    - **Interned strings**: done in dynamic programming languages, where if the strings are the same, they are automatically saved in the same location, so the check can be done with *is* faster than ==, where time complexity is O(n)
    
    in [242. Valid Anagram](anagram.py)
- ***map()* function in Python** : 
    - inputs: map(*func, iter*) where func is a function to pass on each element and iter is an iterable which the function should be mapped 
    - can be used with lambda functions
    - I used it with type conversions as functions to convert datatype
    
    implemented in [Parse string to tuple](parse_string_tuple.py)

## Things to work on (*subjects already looked into are crossed out*)
- namespace in Python
- ~~Calculating Time Complexity and Space Complexity (be aware!)~~