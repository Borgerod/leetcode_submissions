l=[5,9,5,7]
result= []

for i in range(0,len(l)): 
    last_elem = l.pop() 
    result.append(last_elem) 
    l = [i-1 for i in l]
print(result)
