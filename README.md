# Binary Search Tree v2.1.0

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
"""
Welcome to the BinarySearchTree documentation!

A Binary Search Tree (BST) is a fundamental data structure for efficient storage and retrieval of elements. This implementation provides a versatile toolkit for managing BSTs, whether you're storing integers, dictionaries, or custom objects.

Here, you'll find everything you need to know about utilizing BinarySearchTree in your projects. From basic operations like insertion and search to advanced functionalities such as traversal and compatibility checking, this class offers a comprehensive set of methods to handle your data efficiently.

Let's dive in and explore how BinarySearchTree can streamline your coding experience!
"""

from bst import BinarySearchTree as Tree

# It's necessary to pass a data type that supports (>, ==, <).
tree = Tree(int)

# Creating a trivial tree of integers.
# Add integers from 0 to 29 to the tree.
tree.insert(*[n for n in range(30)]) # Equivalent to: for n in range(30): tree.insert(n) 

# Print the height and size of the tree before stabilization.
print("Tree height:", tree.height)  # Returns 30.
print("Tree length:", tree.length)  # Returns 30.
print("Tree is empty:", tree.is_empty) # Returns False
print("Tree type:", tree.type) # Returns <class 'int'>

# Balance the tree.
tree.stabilize()

# Print the height and size of the tree after stabilization.
print("Tree height", tree.height)  # Returns 5.
print("Tree length", tree.length)  # Returns 30.

# Check if an element exists in the tree.
search_result = tree.search(19)  # Equivalent to: 19 in tree, tree.exists(19)
print("Search result for element 19:", search_result)  # Returns true

# Check if multiple elements exist in the tree.
search_result = tree.exists(3, 29, 1, 4)
print("Search result for elements 3, 29, 1, 4:", search_result)  # Returns true


# Remove element 19 from the tree.
tree.remove(19) # Equivalent to: tree -= 19, tree = tree - 19
print("Search result for element 19 after removal:", 19 in tree)  # Returns false

print("Tree length after removal:", tree.length)  # Returns 29

# Returning lists with different orders of traversal.
print("Inorder traversal: ", tree.inorder())
print("Preorder traversal: ", tree.preorder())
print("Postorder traversal: ", tree.postorder())
print("Levelorder traversal: ", tree.levelorder())
print("Spiralorder traversal: ", tree.spiralorder())

# Returning the minimum and maximum elements respectively.
print("Minimum element:", tree.min_value)
print("Maximum element:", tree.max_value)

# Accessing a data item:
n = 3
print("Accessing a data item:", tree[n])  # Equivalent to tree.inorder()[n]

# Iterating over the tree:
for v in tree: print(v) # Equivalent to: for v in tree.inorder(): print(v)

# Subset of trees of the same type:
subtree = Tree(int).insert(3, 10, 2).stabilize() 

subtree.insert(13) # Equivalent to: subtree += 13, subtree = subtree + 13

print("'subtree' is contained in 'tree':", subtree in tree)  # Returns True
print("'subtree == 'tree':", subtree == tree)  # Returns false
print("'tree' is contained in 'subtree':", tree in subtree) # Returns False

subtree += tree # Equivalent to: subtree.insert(*tree)
print("'tree' is contained in 'subtree':", tree in subtree) # Returns True

# Check if elements of 'tree' are compatible with 'subtree'.
print("elements of 'tree' are compatible with 'subtree'", tree.is_compatible(*subtree)) # Returns True | Equivalent to: all(tree.is_compatible(v) for v in subtree)

# Clear the tree and insert new elements.
tree.clear().insert(60, 10, 3, 4, 5) # Clear the tree and insert new elements.

# Check if 60 is in the tree.
print("60 in tree:", 60 in tree) # Returns True

# Remove element 60 from the tree.
tree.remove(60)
# Check if 60 is still in the tree after removal.
print("60 in tree:", 60 in tree) # Returns False

# Remove elements 10, 3, 4, 5 from the tree.
tree.remove(10, 3, 4, 5) 
# Check if the tree is empty after removing all elements.
print("tree is empty:", tree.is_empty) # Returns True

tree = subtree.copy()

subtree.remove(*[n for n in range(5)])

tree -= subtree # Equivalent to: tree.remove(*subtree)

print(tree.stabilize().inorder()) # Returns [0, 1, 2, 3, 4]

print(tree) # Returns 'BST(int):[2, 1, 0, 4, 3]'


# Creating a tree with a custom comparison function to store values
# It is necessary to pass a function that returns a data type that supports (>, ==, <).
tree_dict = Tree(dict, lambda item: item.get('custom_comparison_key')) 


from dataclasses import dataclass

@dataclass
class CustomClass:
    custom_comparison_attribute : int

# Creating a tree with a custom attribute to store values
# It is necessary to pass an attribute of the class that contains a data type that supports (>, ==, <).
tree_class = Tree(CustomClass, 'custom_comparison_attribute')


# Inserting values into the dictionary-based tree
tree_dict.insert(*[{ 'custom_comparison_key': n, 'other': None } for n in range(10)] ).stabilize()

# Inserting values into the class-based tree
tree_class.insert(*[CustomClass(n) for n in range(10)])

# Retrieving values by custom attribute

# Retrieving value from the dictionary-based tree using the custom comparison key
print(tree_dict.search(3))  # Returns { 'custom_comparison_key': 3, 'other': None }

# Retrieving value from the class-based tree using the custom comparison attribute
print(tree_class.search(3))  # Returns instance 'CustomClass(3)'

# Removing a value from the class-based tree
tree_class.remove(3)  # Equivalent to: tree_class.remove(CustomClass(3))

# Removing a value from the dictionary-based tree
tree_dict.remove(3)  # Equivalent to: tree_dict.remove({ 'custom_comparison_key': 3, 'other': None })

print("4 in tree_dict", 4 in tree_dict) # Returns True
print("3 in tree_dict", 3 in tree_dict) # Returns False

# Equivalent to
print("4 in tree_dict", { 'custom_comparison_key': 4, 'other': None } in tree_dict) # Returns True
print("3 in tree_dict", { 'custom_comparison_key': 3, 'other': None } in tree_dict) # Returns False
```

## Contanct

For any inquiries or feedback regarding this project, please contact us on [Discord](https://discord.gg/mjjzur9gBR)