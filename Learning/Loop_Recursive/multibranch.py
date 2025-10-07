from myqueue import Queue

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.child = []

def build_tree(levels, depth=1, value=1, child_size=3):
    if levels < 1:
        raise ValueError("levels must be >= 1")

    if depth > levels:
        return

    node = TreeNode(value)
    for i in range(value*child_size-(child_size-2),value*child_size+2):
        added_node = build_tree(levels=levels,depth=depth+1,value=i,child_size=child_size)
        if added_node is not None:
            node.child.append(added_node)
    return node

def print_order(tree):

    queue = Queue()
    queue.enqueue(tree)

    while queue:
        node = queue.deque()
        print(node.value ,sep=" ")
        if len(node.child) > 0:
            for point in node.child:
                queue.enqueue(point)
mytree = build_tree(levels=3,child_size=4)
print_order(mytree)


