somearr = [6,9,5,1,3,7,8,2,4]


for i in range(len(somearr)):
    current = somearr[i]
    j = i-1
    while j >= 0 and current < somearr[j]:
        somearr[j+1] = somearr[j]
        j -= 1
    somearr[j+1] = current
    
print(somearr)