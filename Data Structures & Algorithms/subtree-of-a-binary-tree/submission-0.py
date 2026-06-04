class Solution:   
    def sameTree (self, node_1: TreeNode, node_2: TreeNode):
        if node_1 is None and node_2 is None:
            return True
        
        if node_1 is None or node_2 is None:
            return False

        if node_1.val != node_2.val:
            return False

        return self.sameTree(node_1.left, node_2.left) and self.sameTree(node_1.right, node_2.right)
        
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if self.sameTree(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)