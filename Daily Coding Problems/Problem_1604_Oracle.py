"""
Given a binary search tree, find the floor and ceiling of a given integer. 
The floor is the highest element in the tree less than or equal to an integer, 
while the ceiling is the lowest element in the tree greater than or equal to an integer.

If either value does not exist, return None.

"""


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None  # Left child
        self.right = None  # Right child

class BinarySearchTree:
    def __init__(self):
        self.root = None  # Root of the BST

    def insert(self, value):
        # Public method to insert a value into the BST
        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        # Helper method to recursively insert a value
        if node is None:
            return TreeNode(value)  # Base case: create a new node
        
        if value < node.value:
            # If value is less than current node, go left
            node.left = self._insert_recursive(node.left, value)
        else:
            # If value is greater than or equal, go right
            node.right = self._insert_recursive(node.right, value)
        
        return node  # Return the (possibly updated) node

    def find_floor(self, value):
        # Public method to find the floor of a value
        return self._find_floor_recursive(self.root, value, None)

    def _find_floor_recursive(self, node, value, floor):
        # Helper method to recursively find the floor
        if node is None:
            return floor  # Base case: return the current floor

        if node.value == value:
            return node.value  # Exact match found

        if node.value > value:
            # If current value is greater, floor must be in left subtree
            return self._find_floor_recursive(node.left, value, floor)
        
        # If current value is less, it's a candidate for floor
        # Continue searching in right subtree
        return self._find_floor_recursive(node.right, value, node.value)

    def find_ceiling(self, value):
        # Public method to find the ceiling of a value
        return self._find_ceiling_recursive(self.root, value, None)

    def _find_ceiling_recursive(self, node, value, ceiling):
        # Helper method to recursively find the ceiling
        if node is None:
            return ceiling  # Base case: return the current ceiling

        if node.value == value:
            return node.value  # Exact match found

        if node.value < value:
            # If current value is less, ceiling must be in right subtree
            return self._find_ceiling_recursive(node.right, value, ceiling)
        
        # If current value is greater, it's a candidate for ceiling
        # Continue searching in left subtree
        return self._find_ceiling_recursive(node.left, value, node.value)

# Test the implementation
bst = BinarySearchTree()
values = [8, 4, 12, 2, 6, 10, 14]
for value in values:
    bst.insert(value)  # Insert values into the BST

# Test cases
test_values = [5, 11, 1, 15]
for value in test_values:
    floor = bst.find_floor(value)  # Find floor
    ceiling = bst.find_ceiling(value)  # Find ceiling
    print(f"For {value}: Floor = {floor}, Ceiling = {ceiling}")