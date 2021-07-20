from itertools import combinations
a = list(map(str,input().split()))
for i in range(1,int(a[1])+1):
    for j in combinations(sorted(a[0]),i):
        print(''.join(map(str, j)))

        
#  HACK 2  -- INPUT
# OUTPUTS
# A 
# C
# H
# K
# AC
# AH
# AK
# CH
# CK
# HK
