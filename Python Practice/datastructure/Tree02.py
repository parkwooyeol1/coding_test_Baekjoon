class TreeNode:
    def __init__(self, val=0, right=None, left=None):
        self.val = val
        self.right = right
        self.left = left
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(9)
root.left.right = TreeNode(7)
root.left.left = TreeNode(7)



from typing import List

class TreeDiameter:
  def solution(self, root: TreeNode) -> int:
    if root is None:
      return 0
    
    self._diameter = 0    
    self._recursiveDepth(root)
    
    return self._diameter
  
  def _recursiveDepth(self, node: TreeNode) -> int:   
    
    left_depth = 0
    right_depth = 0
    if node.left:
      left_depth = self._recursiveDepth(node.left)
    if node.right:
      right_depth = self._recursiveDepth(node.right)
    
    node_diameter = left_depth+right_depth
    self._diameter = max(self._diameter,node_diameter)
    
    node_depth = max(left_depth,right_depth)
    return node_depth+1