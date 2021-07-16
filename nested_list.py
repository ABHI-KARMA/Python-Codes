d={} 
for _ in range(int(input())): 
    Name=input() 
    Grade=float(input()) 
    d[Name]=Grade 
v=d.values()
second=sorted(list(set(v)))[1] 
second_lowest=[] 
for key,value in d.items():  
    if value==second:
        second_lowest.append(key) 
second_lowest.sort() 
for name in second_lowest: 
    print (name)