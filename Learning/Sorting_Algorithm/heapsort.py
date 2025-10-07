"""Start of my implementation"""

def heapify(an_arr):
  for index in range(len(an_arr)-1,0,-1):
      while index > 0:
        parent_index = (index-1)//2

        if an_arr[index] > an_arr[parent_index]:
          an_arr[parent_index],an_arr[index] = an_arr[index],an_arr[parent_index]
          index = parent_index
          
        else:
          break
    
  return an_arr
    
def sort(an_arr):
  for length in range(len(an_arr),0,-1):
    an_arr[0] , an_arr[length-1] = an_arr[length-1] , an_arr[0]
    heap_size = length-1
    index = 0
    while True:
      left,right = index*2+1,index*2+2
      if left >= heap_size:
        break
      
      if right >= heap_size:
        child_index = left
      
      else:
        child_index = left if an_arr[left] > an_arr[right] else right
      
      if an_arr[child_index] > an_arr[index] :
        an_arr[child_index],an_arr[index] = an_arr[index],an_arr[child_index]
        index = child_index
        
      else:
        break
      
  return an_arr

"""End of my implementation"""

"""Chatgpt Better Version"""

def sift_down(arr, start, heap_size):
    """
    Push element at index `start` down until the subtree rooted at start is a valid max-heap.
    Use this implementation instead of bubble-up when working with a full array,
    because it achieves better time complexity (O(n) heapify vs O(n log n) for repeated insertions).
    """
    i = start
    while True:
        left = 2 * i + 1
        if left >= heap_size:
            break
        right = left + 1
        largest = i
        if arr[left] > arr[largest]:
            largest = left
        if right < heap_size and arr[right] > arr[largest]:
            largest = right
        if largest == i:
            break
        arr[i], arr[largest] = arr[largest], arr[i]
        i = largest

def build_heap(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        sift_down(arr, i, n)

def heapsort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    build_heap(arr)
    for heap_size in range(n, 1, -1):
        arr[0], arr[heap_size - 1] = arr[heap_size - 1], arr[0]
        sift_down(arr, 0, heap_size - 1)
    return arr
  
"""The end of chatgpt version"""

if __name__ == "__main__":

  my_arr = [7,8,2,4,1,10,9,6,5,3,11,13,12]
  
  max_arr = heapify(my_arr)
  sorted_arr = sort(max_arr)
  
  print(f"My implementation result: {sorted_arr}")
  
  out = heapsort(my_arr.copy())
  print(f"Chatgpt Result: {out}")

