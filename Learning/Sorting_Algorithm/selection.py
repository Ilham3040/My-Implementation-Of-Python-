somearr = [6,9,5,1,3,7,8,2,4]


for i in range(len(somearr)):
    smallest_index = i
    for j in range(i+1,len(somearr)):
        if somearr[j] < somearr[smallest_index]:
            smallest_index = j
            
    if smallest_index != i:  # only swap if needed
        somearr[i], somearr[smallest_index] = somearr[smallest_index], somearr[i]

print(somearr)