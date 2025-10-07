from myqueue import Queue

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def build_tree(levels, depth=1, value=1):
    if levels < 1:
        raise ValueError("levels must be >= 1")

    if depth > levels:
        return None

    node = TreeNode(value)
    node.left = build_tree(levels, depth + 1, value * 2)
    node.right = build_tree(levels, depth + 1, value * 2 + 1)
    return node

def print_order(tree):

    queue = Queue()
    queue.enqueue(tree)

    while queue:
        node = queue.deque()
        print(node.value ,sep=" ")
        if node.left:
            queue.enqueue(node.left)
        if node.right:
            queue.enqueue(node.right)
            
mytree = build_tree(3)
print_order(mytree)


