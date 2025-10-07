from myqueue import Queue

class TreeNode:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
        
        
class Tree:
    def __init__(self):
        self._tree = None
        
    def build_tree(self,levels):
    
        if levels < 1 :
            print("levels can't be under 1")
            return
        
        total_nodes = 2**levels-1
        nodes = [TreeNode(i) for i in range(1,total_nodes+1)]
        
        for i in range(total_nodes):
            left_index = 2*i+1
            right_index = 2*i+2
            if left_index < total_nodes:
                nodes[i].left = nodes[left_index]
                
            if right_index < total_nodes:
                nodes[i].right = nodes[right_index]
        
        self._tree = nodes[0]
        
    def print_order(self):
        if not self._tree:
            print("this tree is empty")
            return
        
        queue = Queue()
        queue.enqueue(self._tree)

        while queue:
            node = queue.deque()
            print(node.value ,sep=" ")
            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)
        

            
        


    
    