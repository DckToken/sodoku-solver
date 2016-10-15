# sodoku-solver
##Initial board:
```
   #column 0                       #column 8
 ╔═══╤═══╤═══╦═══╤═══╤═══╦═══╤═══╤═══╗
a║   │   │   ║   │   │   ║   │   │   ║ #row 0
 ╟───┼───┼───╫───┼───┼───╫───┼───┼───╢
b║   │   │   ║   │   │   ║   │   │   ║
 ╟───┼───┼───╫───┼───┼───╫───┼───┼───╢
c║   │   │   ║   │   │   ║   │   │   ║
 ╠═══╪═══╪═══╬═══╪═══╪═══╬═══╪═══╪═══╣
d║   │   │   ║   │   │   ║   │   │   ║
 ╟───┼───┼───╫───┼───┼───╫───┼───┼───╢
e║   │   │   ║   │   │   ║   │   │   ║
 ╟───┼───┼───╫───┼───┼───╫───┼───┼───╢
f║   │   │   ║   │   │   ║   │   │   ║
 ╠═══╪═══╪═══╬═══╪═══╪═══╬═══╪═══╪═══╣
g║   │   │   ║   │   │   ║   │   │   ║
 ╟───┼───┼───╫───┼───┼───╫───┼───┼───╢
h║   │   │   ║   │   │   ║   │   │   ║
 ╟───┼───┼───╫───┼───┼───╫───┼───┼───╢
i║   │   │   ║   │   │   ║   │   │   ║ #row 8
 ╚═══╧═══╧═══╩═══╧═══╧═══╩═══╧═══╧═══╝
   1   2   3   4   5   6   7   8   9 

```
##How to store values
Nested lists. I think I need them
```python
#       square 
#         | 
#       column
#     row||
#       |||
board = [[[3, 7, 8],[4, 5, 9],[8, 9, 6]]]
# First square is board[0][0][0]
# Syntax is board[row][column][square]
board = [[[3, 7, 8],[4, 5, 9],[8, 9, 6]],[[2, 8, 4],[5, 6, 9],[2, 4, 5]]]
#That should work too
```
##Proposed board
```
 ╔═══╤═══╤═══╦═══╤═══╤═══╦═══╤═══╤═══╗
a║   │   │ 7 ║   │   │ 1 ║ 3 │   │   ║
 ╟───┼───┼───╫───┼───┼───╫───┼───┼───╢
b║ 3 │   │   ║   │ 5 │   ║ 6 │   │   ║
 ╟───┼───┼───╫───┼───┼───╫───┼───┼───╢
c║ 5 │   │ 8 ║   │ 3 │   ║   │   │ 4 ║
 ╠═══╪═══╪═══╬═══╪═══╪═══╬═══╪═══╪═══╣
d║   │ 8 │   ║   │ 6 │   ║ 9 │   │   ║
 ╟───┼───┼───╫───┼───┼───╫───┼───┼───╢
e║ 7 │   │   ║   │   │   ║   │   │ 6 ║
 ╟───┼───┼───╫───┼───┼───╫───┼───┼───╢
f║   │   │ 4 ║   │ 1 │   ║   │ 7 │   ║
 ╠═══╪═══╪═══╬═══╪═══╪═══╬═══╪═══╪═══╣
g║ 2 │   │   ║   │ 8 │   ║ 4 │   │ 3 ║
 ╟───┼───┼───╫───┼───┼───╫───┼───┼───╢
h║   │   │ 6 ║   │ 7 │   ║   │   │ 8 ║
 ╟───┼───┼───╫───┼───┼───╫───┼───┼───╢
i║   │   │ 5 ║ 9 │   │   ║ 7 │   │   ║
 ╚═══╧═══╧═══╩═══╧═══╧═══╩═══╧═══╧═══╝
   1   2   3   4   5   6   7   8   9
```
(27 clues)
I should use this one for testing purpouses
To Do: convert this to a nested list

##Solving algorithm
[This](https://en.wikipedia.org/wiki/Sudoku_solving_algorithms) is a must read

###Bruteforce
Maybe the easiest way, right? But it will take long so it might be discarded

###Backtracking
Never heard of this. I will read it carefully and write a python implementation with the nested list I currently have. I still don't know how to point data with that nested list

###Exact cover
I think it will take me longer to understand this than to do a brute force algorithm

###Stochastic search
This is probably just try and error-like algorith. Something like brute force, maybe?

###Constraint programming
Wikipedia links to [this](http://4c.ucc.ie/~hsimonis/sudoku.pdf), it might be usefull
