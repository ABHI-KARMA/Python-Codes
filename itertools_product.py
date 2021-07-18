from itertools import product  # import product from itertools
a = map(int,input().split())  # take a list of integer saperated by space 
b = map(int,input().split())  
c = product(a,b)  # called product to do product of two iterables
for i in c:
    print(i,end=' ') # print each saperated by space
