class TreeNode:
    def __init__(self, val=0, right=None, left=None):
        self.val = val
        self.right = right
        self.left = left
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
"""
def preorder(n):
    print(n.val)
    print(n.left.val)
    print(n.right.val)
preorder(root)

def inorder(n):
    print(n.left.val)
    print(n.val)
    print(n.right.val)
inorder(root)

def postorder(n):
    print(n.left.val)
    print(n.right.val)
    print(n.val)
postorder(root)

def inorder1(n):
    if n is not None:
        inorder1(n.left)  
        print(n.val, end=" ")
        inorder1(n.right)
inorder1(root)

def postorder1(n):
    if n is not None:
        inorder1(n.left)
        inorder1(n.right)
        print(n.val, end=" ")
postorder1(root)
"""

from collections import deque

def level_order_traversal(root):
    q = deque()
    q.append(root)
    while q:
        node = q.popleft()
        print(node.val)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
        #q.extend(filter(None, [node.left, node.right]))
level_order_traversal(root)