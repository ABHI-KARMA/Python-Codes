# average of array
def average(array):
    set1 = set(array)
    sum = 0
    for a in set1:
        sum = sum + a
    avg = sum/len(set1)
    return avg
    
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)

# length of set
n = int(input())
l = []
for i in range(0,n):
    j = input()
    l.append(j)
    
s = set(l)
le = len(s)
print(le)
