class TreeNode:
    def __init__(self,isLeaf):
        self.isLeaf = isLeaf
        self.keys = []
        self.childs = []


class B_Tree:
    def __init__(self,t):
        self.t = t
        self.root = TreeNode(isLeaf=True)
        
    def insertion(self,value):
        root = self.root
        if len(root.keys) == 2*self.t-1:
            temp = TreeNode(False)
            self.root = temp
            temp.childs.append(root)
            self.split_child(temp,0)
            self.insertion_if_not_full(temp,value)
            
        else:
            self.insertion_if_not_full(root,value)
    
    def insertion_if_not_full(self,x,value):
        index = len(x.keys)-1
        if x.isLeaf:
            x.keys.append(None)
            while index >= 0 and value < x.keys[index]:
                x.keys[index+1] = x.keys[index]
                index-=1
            x.keys[index+1] = value
        
        else:
            while index >= 0 and value < x.keys[index]:
                index-=1
            index+=1
            if len(x.childs[index].keys) == (2 * self.t) - 1:
                self.split_child(x, index)
                if value > x.keys[index]:
                    index += 1
            self.insertion_if_not_full(x.childs[index],value)
            
            
    def split_child(self, x, i):
        t = self.t
        y = x.childs[i]
        y_keys = y.keys  # reference to original list
        z = TreeNode(y.isLeaf)

        # insert new child and median key into parent
        x.childs.insert(i+1, z)
        median = y_keys[t-1]
        x.keys.insert(i, median)

        # set new key lists (from original snapshot)
        z.keys = y_keys[t:]           # keys after median
        y.keys = y_keys[:t-1]         # keys before median

        # move child pointers if not leaf
        if not y.isLeaf:
            z.childs = y.childs[t:]   # right children
            y.childs = y.childs[:t]   # left children

        

if __name__ == "__main__":
    mytree = B_Tree(2)
    for i in range(1,9):
        mytree.insertion(i*2)
        
    print(mytree.root.keys)
    for i in mytree.root.childs:
        print(i.keys)
    print(mytree.root.isLeaf)
    print(mytree.root.childs[0].isLeaf)