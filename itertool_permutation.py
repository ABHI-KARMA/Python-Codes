from itertools import permutations
b = list(map(str,input().split()))
i,r = b[0],int(b[1])
i = list(i)
for j in permutations(sorted(i),r):
    print(''.join(map(str, j)))
