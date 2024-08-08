"""

This problem was asked by PayPal.

Given a binary tree, determine whether or not it is height-balanced. 
A height-balanced binary tree can be defined as one in which the heights of the two subtrees of any node never differ by more than one.

"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_height_balanced(root: TreeNode) -> bool:
    """
    Determine whether the given binary tree is height-balanced.
    
    A height-balanced binary tree is defined as a binary tree in which the heights of the two subtrees of any node never differ by more than one.
    
    Args:
        root (TreeNode): The root of the binary tree.
    
    Returns:
        bool: True if the binary tree is height-balanced, False otherwise.
    """
    def get_height(node: TreeNode) -> int:
        """
        Helper function to get the height of a given node in the binary tree.
        
        Args:
            node (TreeNode): The node whose height is to be determined.
        
        Returns:
            int: The height of the given node, or -1 if the tree is not height-balanced.
        """
        # Base case: If the node is None, the height is 0
        if not node:
            return 0
        
        # Recursively compute the height of the left and right subtrees
        left_height = get_height(node.left)
        right_height = get_height(node.right)
        
        # If either the left or right subtree is not height-balanced, return -1
        if left_height == -1 or right_height == -1 or abs(left_height - right_height) > 1:
            return -1
        
        # Otherwise, return the maximum height of the two subtrees plus 1 (the height of the current node)
        return max(left_height, right_height) + 1
    
    # Call the helper function on the root of the tree
    # If the return value is not -1, the tree is height-balanced
    return get_height(root) != -1