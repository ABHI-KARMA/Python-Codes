from itertools import combinations_with_replacement  # Imported 

b = list(map(str,input().split()))   # take 2 space saperated user input
for i in combinations_with_replacement(sorted(b[0]),int(b[1])):  # iterate over combinations
    print("".join(map(str,i))) #join
