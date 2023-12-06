'''
   You are appointed to a very important task: you are in charge of flattening one specific road.

The road can be represented as a polygonal line starting at (0,0)
, ending at (n−1,0)
 and consisting of n
 vertices (including starting and ending points). The coordinates of the i
-th vertex of the polyline are (i,ai)
.

"Flattening" road is equivalent to choosing some line segment from (0,y0)
 to (n−1,y1)
 such that all points of the polyline are below the chosen segment (or on the same height). Values y0
 and y1
 may be real.

You can imagine that the road has some dips and pits, and you start pouring pavement onto it until you make the road flat. Points 0
 and n−1
 have infinitely high walls, so pavement doesn't fall out of segment [0,n−1]
.


The cost of flattening the road is equal to the area between the chosen segment and the polyline. You want to minimize the cost, that's why the flattened road is not necessary horizontal.

But there is a problem: your data may be too old, so you sent a person to measure new heights. The person goes from 0
 to n−1
 and sends you new heights bi
 of each vertex i
 of the polyline.

Since measuring new heights may take a while, and you don't know when you'll be asked, calculate the minimum cost (and corresponding y0
 and y1
) to flatten the road after each new height bi
 you get.

Input
The first line contains a single integer n
 (3≤n≤2⋅105
) — the number of vertices of the polyline.

The second line contains n
 integers a0,a1,…,an−1
 (0≤ai≤109
; a0=an−1=0
) — the heights of the corresponding vertices.

The third line contains n
 integers b0,b1,…,bn−1
 (0≤bi≤109
; b0=bn−1=0
) — the new heights of the corresponding vertices.

Output
Print n
 numbers: as the i
-th number (0
-indexed) print y0+y1
 of the "best segment" (i. e. the sum of coordinates of the segment that gives the minimum cost) if you already know actual heights b0,…,bi
.

If there are several "best segments", print the minimum possible y0+y1
 among them.

Your answer is considered correct if its absolute or relative error does not exceed 10−9
.

Formally, let your answer be x
, and the jury's answer be y
. Your answer is accepted if and only if |x−y|max(1,|y|)≤10−9
.
'''