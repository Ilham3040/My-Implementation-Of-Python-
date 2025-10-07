class Queue:
    def __init__(self,data=[]):
        self._data = data
        self._head = 0
        
    def __len__(self):
        return len(self._data) - self._head
    
    def __bool__(self):
        # Queue is True if there are still elements
        return len(self) > 0
    
    def enqueue(self,value):
        self._data.append(value)
        
    def deque(self):
        if self._head >= len(self._data):
            raise IndexError("dequeue from empty queue")
        
        first_out = self._data[self._head]
        self._head += 1
        
        if self._head >= 8 and self._head >= len(self._data) // 2:
            self._data = self._data[self._head:]
            self._head = 0
        
        return first_out
        
    def printout(self):
        return self._data[self._head:]
        