import unsorted
somearr = unsorted.shuffled_array

def quicksort(arr):
    if len(arr) <= 1 :
        return arr
    
    pivot = arr[-1]
    
    left = [i for i in arr if i < pivot]
    right = [i for i in arr if i > pivot]
    middle = [i for i in arr if i == pivot]
    
    return quicksort(left) + middle + quicksort(right)

somearr = quicksort(somearr)

print(somearr)