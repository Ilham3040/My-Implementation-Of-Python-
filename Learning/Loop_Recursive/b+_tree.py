class TreeNode:
    def __init__(self, is_leaf):           
        self.is_leaf = is_leaf     
        self.keys = []             
        self.values = []          
        self.children = []       
        self.next = None           
        self.parent = None       
        
        
class BPlusTree:
    def __init__(self,t):
        self.root = TreeNode(True)
        self.t = t
        
    def insert_item(self,key,value):
        value = str(value)
        current_node = self.to_the_leaf(key)
        self.insert_values(current_node,key,value)
        
        if len(current_node.keys) == self.t*2:
            addnew_node = TreeNode(True)
            addnew_node.parent = current_node.parent
            addnew_node.keys = current_node.keys[self.t:]
            addnew_node.values = current_node.values[self.t:]
            current_node.keys = current_node.keys[:self.t]
            current_node.values = current_node.values[:self.t]
            current_node.next = addnew_node
            
            self.insert_to_parent(current_node,current_node.keys[self.t-1],addnew_node)
            
    def insert_to_parent(self,left,mid_key,right):
        if left == self.root:
            new_node = TreeNode(False)
            new_node.keys = [mid_key]
            new_node.children = [left,right]
            self.root = new_node
            left.parent = new_node
            right.parent = new_node
            
            return
        
        parentNode = left.parent
        temp = parentNode.keys
        for i in range(len(temp)):
            if mid_key <= temp[i]:
                parentNode.keys = parentNode.keys[:i] + [mid_key] + parentNode.keys[i:]
                parentNode.children = parentNode.children[:i] + [right] + parentNode.children[i:]
                
            elif i+1 == len(temp):
                parentNode.keys.append(mid_key)
                parentNode.children.append(right)

        if len(parentNode.keys) == self.t*2:
            addnew_node = TreeNode(False)
            addnew_node.parent = parentNode.parent
            addnew_node.keys = parentNode.keys[self.t:]
            addnew_node.children = parentNode.children[self.t:]
            parentNode.keys = parentNode.keys[:self.t]
            parentNode.children = parentNode.children[:self.t]
            for i in addnew_node.children: i.parent = addnew_node
            self.insert_to_parent(parentNode,parentNode.keys[self.t-1],addnew_node)
                
    def insert_values(self,node,key,value):
        if node.keys:
            temp = node.keys
            for i in range(len(temp)):
                
                if key <= temp[i]:
                    node.keys = node.keys[:i] + [key] + node.keys[i:]
                    node.values = node.values[:i] + [value] + node.values[i:]
                    
                elif i+1 == len(temp):
                    node.keys.append(key)
                    node.values.append(value)
                    
        else:
            node.keys = [key]
            node.values = [value]
                    

    def to_the_leaf(self,key):
        current_nodes = self.root
        while current_nodes.is_leaf == False:
            temp  = current_nodes.keys
            for i in range(len(temp)):
                
                if key <= temp[i]:
                    current_nodes = current_nodes.children[i]
                    break
                    
                elif i+1 == len(temp):
                    current_nodes = current_nodes.children[i+1]
                    break
        return current_nodes
    
    def getting_value(self,key):
        current_nodes = self.to_the_leaf(key)
        for i in range(len(current_nodes.keys)):
            if current_nodes.keys[i] == key:
                return current_nodes.values[i]
        return "The selected key not found"
    
    def getting_range_of_values(self,key,ranges):
        bunch_word = []
        start_index = None
        current_nodes = self.to_the_leaf(key)
        for i in range(len(current_nodes.keys)):
            if current_nodes.keys[i] == key:
                bunch_word.append(current_nodes.values[i])
                start_index = i+1
                break
            
        while bunch_word != ranges:
            for i in range(start_index,len(current_nodes.keys)):
                bunch_word.append(current_nodes.values[i])
                if len(bunch_word) == ranges:
                    return bunch_word
            start_index = 0
            current_nodes = current_nodes.next

        return "Its bigger than the tree max key"
            
            
    
    
    
if __name__ == "__main__" :
    my_tree = BPlusTree(3)
    
    my_line = f"""
    Embraced by the flames I can not see anything right now
    But the memories of my home forever remains
    There is no way back now
    Here is my grave, how why I wish I could
    """
    my_arr = my_line.split()
    
    for i in range(len(my_arr)):
        my_tree.insert_item(i+1,my_arr[i])
    # print(my_tree.root.children[0].keys)
    # for i in my_tree.root.children:
    #     for j in i.children:
    #         print(j.keys)
    print(my_tree.getting_value(2))
    print(my_tree.getting_range_of_values(2,20))
