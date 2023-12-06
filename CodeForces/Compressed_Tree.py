'''
   You are given a tree consisting of n
 vertices. A number is written on each vertex; the number on vertex i
 is equal to ai
.

You can perform the following operation any number of times (possibly zero):

choose a vertex which has at most 1
 incident edge and remove this vertex from the tree.
Note that you can delete all vertices.

After all operations are done, you're compressing the tree. The compression process is done as follows. While there is a vertex having exactly 2
 incident edges in the tree, perform the following operation:

delete this vertex, connect its neighbors with an edge.
It can be shown that if there are multiple ways to choose a vertex to delete during the compression process, the resulting tree is still the same.

Your task is to calculate the maximum possible sum of numbers written on vertices after applying the aforementioned operation any number of times, and then compressing the tree.

Input
The first line contains a single integer t
 (1≤t≤104
) — the number of test cases.

The first line of each test case contains a single integer n
 (2≤n≤5⋅105
) — the number of vertices.

The second line contains n
 integers a1,a2,…,an
 (−109≤ai≤109
).

Each of the next n−1
 lines describes an edge of the tree. Edge i
 is denoted by two integers vi
 and ui
, the labels of vertices it connects (1≤vi,ui≤n
, vi≠ui
). These edges form a tree.

Additional constraint on the input: the sum of n
 over all test cases doesn't exceed 5⋅105
.

Output
For each test case, print a single integer — the maximum possible sum of numbers written on vertices after applying the aforementioned operation any number of times, and then compressing the tree.
'''