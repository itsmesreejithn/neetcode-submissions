# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        same_tree: bool = True
        
        def dfs(node_1: TreeNode, node_2: TreeNode):
            nonlocal same_tree

            if node_1 is None and node_2 is None:
                return

            if node_1 is None or node_2 is None:
                same_tree = False
                return

            if node_1.val != node_2.val:
                same_tree = False
                return

            dfs(node_1.left, node_2.left)
            dfs(node_1.right, node_2.right)

        dfs(p, q)

        return same_tree

            