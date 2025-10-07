
def insertion(heap_arr,value,order):
  heap_order = {
    "min" : lambda x,y : x < y,
    "max" : lambda x,y : x > y
  }
  heap_arr.append(value)
  item_index = len(heap_arr)-1
  while item_index > 0:
    parent_index = (item_index-1)//2

    if heap_order[order](heap_arr[item_index],heap_arr[parent_index]):
      heap_arr[parent_index],heap_arr[item_index] = heap_arr[item_index],heap_arr[parent_index]
      item_index = parent_index
      
    else:
      break
    
  return heap_arr
    
def pop(heap_arr,order):
  heap_order = {
    "min" : lambda x,y : x < y,
    "max" : lambda x,y : x > y
  }
  selected_value = heap_arr[0]
  heap_arr[0] = heap_arr.pop()
  index = 0 

  while True:
    left,right = index*2+1,index*2+2
    if left >= len(heap_arr):
      break
    
    if right >= len(heap_arr):
      child_index = left
    
    else:
      child_index = left if heap_order[order](heap_arr[left],heap_arr[right]) else right
    
    if heap_order[order](heap_arr[child_index],heap_arr[index]):
      heap_arr[child_index],heap_arr[index] = heap_arr[index],heap_arr[child_index]
      index = child_index
      
    else:
      break
    
  return heap_arr,selected_value
    
    

my_arr = [7,8,2,4,1,10,9,6,5,3]

min_arr = []
max_arr = []

for i in my_arr:
  min_arr = insertion(min_arr,i,"min")
  
for i in my_arr:
  max_arr = insertion(max_arr,i,"max")

print(max_arr)

for i in range(6):
  max_arr,value = pop(max_arr,"max")
  print(value)
  print(max_arr)