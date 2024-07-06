# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def inOrder(root):
            if root is None:
                return []
            return(inOrder(root.left),[root.val],inOrder(root.right))
        if inOrder(p)==inOrder(q):
            return True
        else:
            return False

        