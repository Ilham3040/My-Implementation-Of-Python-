my_things = [1,5,7,8,12,17,21,22,24,30]

def search(arr,value):
    low,high = 0,len(arr)-1

    while low <= high:
        mid = (low+high) // 2
        if value < arr[mid]:
            high = mid-1
            
        elif value > arr[mid]:
            low = mid+1
        else:
            return arr[mid]
            
    
    return "Item not found"
    

        
    
    
print(search(my_things,11))