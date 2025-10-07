# tree.py
from collections import deque
from itertools import count
from typing import Any, Callable, Optional, List

class Node:
    def __init__(self, value: Any):
        self.value: Any = value
        self.children: List["Node"] = []

    def __repr__(self):
        return f"Node({self.value!r})"


def build_tree(levels: int, branching: int = 3, current_depth: int = 1, id_counter: Optional[count] = None) -> Node:

    if levels < 1:
        raise ValueError("levels must be >= 1")
    if branching < 1:
        raise ValueError("branching must be >= 1")

    if id_counter is None:
        id_counter = count(1)

    node_value = next(id_counter)
    node = Node(node_value)

    if current_depth == levels:
        return node

    for _ in range(branching):
        child = build_tree(levels, branching, current_depth + 1, id_counter)
        node.children.append(child)

    return node


def bfs_print(root: Optional[Node], visit: Callable[[Any], None] = print) -> None:
    if root is None:
        return

    q = deque([root])
    while q:
        node = q.popleft()
        visit(node.value)
        for c in node.children:
            q.append(c)


def dfs_preorder(root: Optional[Node], visit: Callable[[Any], None] = print) -> None:
    if root is None:
        return
    visit(root.value)
    for c in root.children:
        dfs_preorder(c, visit)


if __name__ == "__main__":
    tree = build_tree(levels=3, branching=4)   # levels=3, 4 children per node
    print("BFS order:")
    bfs_print(tree)
    print("\nDFS preorder:")
    dfs_preorder(tree)
