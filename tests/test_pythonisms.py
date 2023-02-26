import pytest
from pythonisms import BST, Node



def test_get_nodes(tree1):
    actual = tree1.get_values()
    expected = [1, 2, 4, 5]

    actual == expected


#@pytest.mark.skip
def test_insert_node(tree1):
    tree1.insert(3)
    actual = tree1.get_values()
    expected = [1, 2, 3, 4, 5]

    assert actual == expected


@pytest.fixture
def tree1():
    #       (4)
    #      /   \
    #    (2)   (5)
    #    / \   / \
    #  (1)


    node1 = Node(1)
    node2 = Node(2)
    node4 = Node(4)
    node5 = Node(5)

    node4.left = node2
    node4.right = node5
    node2.left = node1

    tree = BST(node4)
    return tree
