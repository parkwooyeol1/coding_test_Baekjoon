class TreeNode:
    def __init__(self, val=0, right=None, left=None):
        self.val = val
        self.right = right
        self.left = left
root = TreeNode(2)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.left.left = TreeNode(4)
root.left.right = TreeNode(1)
root.right.right = TreeNode(5)

class Solution:
    result = 0
    def longestUnivaluePath(self, root) -> int:
        def dfs(node):
            if not node:
                return 0
        
            left = dfs(node.left)
            if node.left and node.left.val == node.val:
                left += 1
            else:
                left = 0
            
            right = dfs(node.right)
            if node.right and node.right.val == node.val:
                right += 1
            else:
                right = 0
        
            self.result = max(self.result, left + right)
            return max(left, right)
        
        dfs(root)
        return self.result

class Solution:
    long = 0
    def diameterOfBinaryTree(self, root) -> int:

        def dfs(root):
            if not root:
                return -1
            
            left = dfs(root.left)
            right = dfs(root.right)
            self.long = max(self.long, left + right + 2)

            return max(left, right) + 1
        

        dfs(root)
        return self.long