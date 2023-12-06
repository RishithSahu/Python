'''
   You are given an integer array a1,a2,…,an
 (0≤ai≤109
). In one operation, you can choose an integer x
 (0≤x≤1018
) and replace ai
 with ⌊ai+x2⌋
 (⌊y⌋
 denotes rounding y
 down to the nearest integer) for all i
 from 1
 to n
. Pay attention to the fact that all elements of the array are affected on each operation.

Print the smallest number of operations required to make all elements of the array equal.

If the number of operations is less than or equal to n
, then print the chosen x
 for each operation. If there are multiple answers, print any of them.

Input
The first line contains a single integer t
 (1≤t≤104
) — the number of testcases.

The first line of each testcase contains a single integer n
 (1≤n≤2⋅105
).

The second line contains n
 integers a1,a2,…,an
 (0≤ai≤109
).

The sum of n
 over all testcases doesn't exceed 2⋅105
.

Output
For each testcase, print the smallest number of operations required to make all elements of the array equal.

If the number of operations is less than or equal to n
, then print the chosen x
 for each operation in the next line. If there are multiple answers, print any of them.
'''