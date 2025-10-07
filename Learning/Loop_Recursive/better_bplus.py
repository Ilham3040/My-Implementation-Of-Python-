# bplustree_improved.py
from bisect import bisect_left, bisect_right
from typing import Any, List, Optional


class TreeNode:
    def __init__(self, is_leaf: bool):
        self.is_leaf = is_leaf
        self.keys: List[Any] = []
        self.values: List[Any] = []         # used only for leaves (parallel to keys)
        self.children: List["TreeNode"] = []  # used only for internal nodes
        self.next: Optional["TreeNode"] = None
        self.parent: Optional["TreeNode"] = None


class BPlusTree:
    def __init__(self, t: int):
        if t < 2:
            raise ValueError("t (min degree) must be >= 2")
        self.t = t
        self.max_keys = 2 * t - 1
        self.root = TreeNode(is_leaf=True)

    # --- traversal helpers ---
    def _find_leaf(self, key) -> TreeNode:
        node = self.root
        while not node.is_leaf:
            i = bisect_left(node.keys, key)
            node = node.children[i]
        return node

    # --- insertion of single key/value (replace if key exists) ---
    def insert(self, key, value):
        leaf = self._find_leaf(key)
        i = bisect_left(leaf.keys, key)
        if i < len(leaf.keys) and leaf.keys[i] == key:
            # replace policy
            leaf.values[i] = value
            return

        leaf.keys.insert(i, key)
        leaf.values.insert(i, value)

        if len(leaf.keys) > self.max_keys:
            self._split_leaf(leaf)

    def _split_leaf(self, leaf: TreeNode):
        split = len(leaf.keys) // 2
        right = TreeNode(is_leaf=True)
        right.keys = leaf.keys[split:]
        right.values = leaf.values[split:]
        left_keys = leaf.keys[:split]
        left_values = leaf.values[:split]

        # link
        right.next = leaf.next
        leaf.next = right

        # assign left
        leaf.keys = left_keys
        leaf.values = left_values

        # parent linking
        right.parent = leaf.parent

        # promote separator = first key of right
        sep = right.keys[0]
        self._insert_into_parent(leaf, sep, right)

    def _insert_into_parent(self, left: TreeNode, key_for_parent, right: TreeNode):
        if left is self.root:
            # create new root
            new_root = TreeNode(is_leaf=False)
            new_root.keys = [key_for_parent]
            new_root.children = [left, right]
            left.parent = new_root
            right.parent = new_root
            self.root = new_root
            return

        parent = left.parent
        idx = bisect_left(parent.keys, key_for_parent)
        parent.keys.insert(idx, key_for_parent)
        parent.children.insert(idx + 1, right)
        right.parent = parent

        if len(parent.keys) > self.max_keys:
            self._split_internal(parent)

    def _split_internal(self, node: TreeNode):
        mid = len(node.keys) // 2
        # promote node.keys[mid] upward (single key)
        promote = node.keys[mid]

        left_keys = node.keys[:mid]
        right_keys = node.keys[mid + 1:]

        left_children = node.children[: mid + 1]
        right_children = node.children[mid + 1 :]

        right = TreeNode(is_leaf=False)
        right.keys = right_keys
        right.children = right_children
        for c in right_children:
            c.parent = right

        # mutate current node to left
        node.keys = left_keys
        node.children = left_children

        # set parents
        parent = node.parent
        right.parent = parent

        # insert promote into parent
        if node is self.root:
            new_root = TreeNode(is_leaf=False)
            new_root.keys = [promote]
            new_root.children = [node, right]
            node.parent = new_root
            right.parent = new_root
            self.root = new_root
        else:
            # insert promote into parent
            idx = bisect_left(parent.keys, promote)
            parent.keys.insert(idx, promote)
            parent.children.insert(idx + 1, right)
            if len(parent.keys) > self.max_keys:
                self._split_internal(parent)

    # --- lookup ---
    def get(self, key):
        leaf = self._find_leaf(key)
        i = bisect_left(leaf.keys, key)
        if i < len(leaf.keys) and leaf.keys[i] == key:
            return leaf.values[i]
        raise KeyError("Key not found")

    # --- range: start at key (inclusive) and collect up to `count` values ---
    def get_range(self, start_key, count: int):
        if count <= 0:
            return []
        leaf = self._find_leaf(start_key)
        i = bisect_left(leaf.keys, start_key)
        results = []
        node = leaf
        idx = i
        while node is not None and len(results) < count:
            while idx < len(node.keys) and len(results) < count:
                results.append(node.values[idx])
                idx += 1
            node = node.next
            idx = 0
        return results

    # --- debug / traversal helpers ---
    def dump_leaves(self):
        # return list of lists of keys for debugging
        node = self.root
        while not node.is_leaf:
            node = node.children[0]
        out = []
        while node:
            out.append(list(node.keys))
            node = node.next
        return out


if __name__ == "__main__":
    my_tree = BPlusTree(3)
    
    my_line = f"""
    Embraced by the flames I can not see anything right now
    But the memories of my home forever remains
    There is no way back now
    Here is my grave, how why I wish I could
    """
    my_arr = my_line.split()
    
    for i in range(len(my_arr)):
        my_tree.insert(i+1,my_arr[i])

    print("leaves:", my_tree.dump_leaves())
    print("get 2 ->", my_tree.get(2))
    print("range from 2 count 5 ->", my_tree.get_range(2, 30))
