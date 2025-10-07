shuffled_array = [i for i in range(0,502)]

for i in range(len(shuffled_array)// 5):
    for j in range(len(shuffled_array[:i*5])):
        shuffled_array[j] , shuffled_array[~j] = shuffled_array[~j] , shuffled_array[j]
        
        
if __name__ == "__main__":
    print(shuffled_array)