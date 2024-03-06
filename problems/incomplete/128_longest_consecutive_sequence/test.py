subnums =[0, 1, 2, 3, 4, 5, 6, 7, 8]
print(subnums)
for _, y_ in  enumerate(subnums):
    if y_+2 > len(subnums):
        break
    next_y = subnums[-(y_+2)]
    max_y = subnums[-(y_+1)] 
    print(next_y, max_y)