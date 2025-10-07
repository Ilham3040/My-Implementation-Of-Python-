somearr = [6,9,5,1,3,7,8,2,4]

done = False

while (not done):
    passes = 0
    for index, item in enumerate(somearr):
        if index+1 < len(somearr) and item > somearr[index+1]:
            somearr[index], somearr[index+1] = somearr[index+1], somearr[index]
            passes += 1
    if passes == 0:
        done = True
    
print(somearr)