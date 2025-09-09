class TreeNode:
    def __init__(self, val=0, right=None, left=None):
        self.val = val
        self.right = right
        self.left = left
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.left.left = TreeNode(15)
root.left.right = TreeNode(7)

import collections 
def count_node(root):
    if not root:
        return 0
    q = collections.deque([root])
    cnt = 0
    while q:
        node = q.popleft()
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
        if not node.left and not node.right:
            cnt += 1
    return cnt
print(count_node(root))