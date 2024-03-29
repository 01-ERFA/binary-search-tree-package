# Binary Search Tree

## Description

This project implements a Binary Search Tree (BST) data structure in Python. A BST is a binary tree in which all the nodes follow the property that the value of the left child is less than or equal to the parent node, and the value of the right child is greater than or equal to the parent node. This allows for efficient search, insertion, and deletion operations.

## Utility

The Binary Search Tree data structure is useful for organizing and managing data efficiently, especially when it comes to searching for elements within a dataset. It provides logarithmic time complexity for search operations, making it ideal for applications requiring fast retrieval of data.

## Install

You can install the `binary-search-tree` package via pip:

```bash
pip install ran-bst
```

## Examples of Basic Uses

```py
from bst import BinarySearchTree as Tree

# It's necessary to pass a data type that supports (>, ==, <).
tree = Tree(int)  

# Creating a trivial tree of integers.
# Add integers from 0 to 29 to the tree.
for num in range(30): tree.add(num)

# Print the height and size of the tree before stabilization.
print("Tree height", tree.height())  # Returns 30.
print("Tree size", tree.size())  # Returns 30.

# Balance the tree.
tree.stabilize()

# Print the height and size of the tree after stabilization.
print("Tree height", tree.height())  # Returns 5.
print("Tree size", tree.size())  # Returns 30.

# Check if an element exists in the tree.
search_result = tree.exist(19)  # Equivalent to: 19 in tree
print("Search result for element 19:", search_result)  # Returns true

# Remove element 19 from the tree.
tree.remove(19)
print("Search result for element 19 after removal:", 19 in tree)  # Returns false

print("Tree size after removal:", tree.size())  # Returns 29


# Returning lists with different orders of traversal.
print("Inorder traversal: ", tree.inorder())
print("Preorder traversal: ", tree.preorder())
print("Postorder traversal: ", tree.postorder())
print("Levelorder traversal: ", tree.levelorder())
print("Spiralorder traversal: ", tree.spiralorder())

# Returning the minimum and maximum elements respectively.
print("Minimum element:", tree.min())
print("Maximum element:", tree.max())

# Accessing a data item:
n = 3
print("Accessing a data item:", tree[n])  # Equivalent to tree.get(n), tree.inorder()[n]

# Iterating over the tree:
for v in tree: print(v) # Equivalent to: for v in tree.inorder(): print(v)

# Subset of trees of the same type:
subtree = Tree(int)

subtree.add(3)
subtree.add(2)
subtree.add(1)

print("'subtree' is contained in 'tree':", subtree in tree)  # Returns true
print("'subtree == 'tree':", subtree == tree)  # Returns false
print("'tree' is contained in 'subtree':", tree in subtree) # Returns false
```


## Contanct

For any inquiries or feedback regarding this project, please contact us on [Discord](https://discord.gg/mjjzur9gBR)