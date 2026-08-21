# [Educational Round 169 (Div. 2)](https://codeforces.com/contest/2004)

[Problem - D - Codeforces](https://codeforces.com/contest/2004/problem/D)

There are $n$ cities located on a straight line. The cities are numbered from $1$ to $n$.

Portals are used to move between cities. There are $4$ colors of portals: blue, green, red, and yellow. Each city has portals of two different colors. You can move from city $i$ to city $j$ if they have portals of the same color (for example, you can move between a "blue-red" city and a "blue-green" city). This movement costs $|i-j|$ coins.

Your task is to answer $q$ independent queries: calculate the minimum cost to move from city $x$ to city $y$.

> 记录每种颜色组合有哪些地方（map实现），对于$x、y$若能直接跳就直接跳，若不能则去寻找中转站。
>
> 若$[x+1,y-1]$中有中转站那么那么答案为$y-x$。这一步判断用**前缀和**实现。
>
> 再去可能的中转站中寻找位置在$[1,x-1]、[y + 1,n]$中最近的中转站，这一步用**二分查找**实现。

> TODO：补充实现并用样例验证。

