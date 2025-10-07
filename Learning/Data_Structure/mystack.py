class Stack:
    def __init__(self,data=[]):
        self._data = data
        
    def len(self):
        return len(self._data)
    
    def append(self,value):
        self._data.append(value)
        
    def pop(self):
        self._data.pop()
        
    def printout(self):
        print(self._data)
        


if __name__ == "__main__":
    mystack = Stack([i for i in range(1,5)])
    mystack.printout()
    mystack.append(6)
    mystack.printout()
    mystack.pop()
    mystack.printout()
    print(mystack.len())