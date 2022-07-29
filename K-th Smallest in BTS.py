# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorder_travers(node):
            nonlocal node_values
            
            if node is None:
                return
            
            inorder_travers(node.left)
            node_values.append(node.val)
            inorder_travers(node.right)
            
        node_values = []
        inorder_travers(root)
        return node_values[k-1]
            
        