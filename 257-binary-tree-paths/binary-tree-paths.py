# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        lis=[]
        if root==None:
            return []
        if (root.left==None) and (root.right==None):
            return [str(root.val)]
        for leftchild in self.binaryTreePaths(root.left):
            lis.append(str(root.val)+"->"+leftchild)
        for rightchild in self.binaryTreePaths(root.right):
            lis.append(str(root.val)+"->"+rightchild)
        return lis        
           
