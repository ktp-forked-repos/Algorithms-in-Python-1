# Adjacency lists
a, b, c, d, e, f, g, h = range(8)
N = [
    [b, c, d, e, f], # a
    [c, e], # b
    [d], # c
    [e], # d
    [f], # e
    [c, g, h], # f
    [f, h], # g
    [f, g] # h
]

# Adjacency dicts with Edge Weights
a, b, c, d, e, f, g, h = range(8)
N = [
    {b:2, c:1, d:3, e:9, f:4}, # a
    {c:4, e:3}, # b
    {d:8}, # c
    {e:7}, # d
    {f:5}, # e
    {c:2, g:2, h:2}, # f
    {f:1, h:6}, # g
    {f:9, g:8} # h
]

# A Dict with Adjacency Sets
N = {
    'a': set('bcdef'),
    'b': set('ce'),
    'c': set('d'),
    'd': set('e'),
    'e': set('f'),
    'f': set('cgh'),
    'g': set('fh'),
    'h': set('fg')
}

# An Adjacency Matrix, Implemented with Nested Lists
a, b, c, d, e, f, g, h = range(8)
N = [[0,1,1,1,1,1,0,0],
[0,0,1,0,1,0,0,0],
[0,0,0,1,0,0,0,0],
[0,0,0,0,1,0,0,0],
[0,0,0,0,0,1,0,0],
[0,0,1,0,0,0,1,1],
[0,0,0,0,0,1,0,1],
[0,0,0,0,0,1,1,0]]

# A Weight Matrix with Infinite Weight for Missing Edges
a, b, c, d, e, f, g, h = range(8)
_ = float('inf')
W = [[0,2,1,3,9,4,_,_],
[_,0,4,_,3,_,_,_],
[_,_,0,8,_,_,_,_],
[_,_,_,0,7,_,_,_],
[_,_,_,_,0,5,_,_],
[_,_,2,_,_,0,2,2],
[_,_,_,_,_,1,0,6],
[_,_,_,_,_,9,8,0]]
