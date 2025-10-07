art = [1,2,3,4,5]

def add_last(arr,item):
  arr = arr + [item]
  return arr

def add_first(arr,item):
  arr = arr + [None]
  for i in range(len(arr)-1,0,-1):
    arr[i] = arr[i-1]
  arr[0] = item
  return arr

def get_last(arr):
  value = arr[-1]
  arr = arr[:len(arr)-1]
  return arr,value

def get_first(arr):
  value = arr[0]
  arr = arr[1:]
  return arr,value

art,last = get_last(art)
art = add_last(art,12)
print(art)
art,first = get_first(art)
art = add_first(art,13)
print(art)
print(first,last)