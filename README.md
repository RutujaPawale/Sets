Implement Set Operations

Objectives:
To introduce basics of Sets and its operations.
To understand and implement the Array.
To understand how to pass arrays as parameters to functions

Problem Statement:
In a computer engineering class, group A students play cricket, group B students play badminton and group C students play football. Write a python program using functions to compute following: -
a) List of students who play both cricket and badminton
b) List of students who play either cricket or badminton but not both
c) Number of students who play neither cricket nor badminton
d) Number of students who play cricket and football but not badminton.
(Note-Do not use SET builtin functions)

Theory:
Sets:
Python‟s built-in set type has the following characteristics:
-- Sets are unordered.
-- Set elements are unique. Duplicate elements are not allowed.
-- A set itself may be modified, but the elements contained in the set must be of an immutable type

Input:
Input 3 sets of students playing cricket, badminton and football.

Output:
Union
A = { Dwiti, Sahil, Snigdha, Pranjul } B = { Sahil, Sidhant, Snigdha, Anisha}
A U B = { Dwiti, Sahil, Snigdha, Pranjul, Sidhant, Anisha }
Intersection
A = { Dwiti, Sahil, Snigdha, Pranjul } B = { Sahil, Sidhant, Snigdha, Anisha}
A c B = { Sahil, Snigdha}
Difference
A = { Dwiti, Sahil, Snigdha, Pranjul } B = { Sahil, Sidhant, Snigdha, Anisha}
A - B = { Dwiti, Pranjul}
Difference
A = { Dwiti, Sahil, Snigdha, Pranjul } B = { Sahil, Sidhant, Snigdha, Anisha}
B - A = {Sidhant, Anisha }
