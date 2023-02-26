## Iterable Binary Search Tree

### About

This project implements a Binary Search Tree class and Node class for constructing binary search trees. It supports 
the following methods:

insert(value) - inserts value in the BST if not already there, preserving sorted order, and returns the value

get_values() - returns a list of values in order

print_levels() - returns a string reprsenting the nodes in each level of the BST

Magic Methods:

iter - BST's constructed from this class are iterable and can be used with a for in loop and with list 
comprehension.

eq - checks if 2 BST's are equal using == or !=


### Run

pytest tests/test_pythonisms.py


### Acknowledgements

Learned about recursive tree algorithms from neetcode.io