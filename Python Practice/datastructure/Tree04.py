class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# 삽입
def insert(root, val):
    if root is None:
        return TreeNode(val)
    if val < root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)
    return root
# 탐색
def search(root, val):
    if root is None or root.val == val:
        return root
    if val < root.val:
        return search(root.left, val)
    else:
        return search(root.right, val)
# 1. 리프 노드 삭제
def delete_leaf_node(root):
    return None  # 그냥 없애면 됨
# 2. 자식 1개인 노드 삭제
def delete_single_child_node(root):
    return root.left if root.left else root.right  # 자식 1개를 끌어올림
# 3. 자식 2개인 노드 삭제
def delete_two_children_node(root):
    # 중위 후속자(inorder successor)를 찾음: 오른쪽 서브트리에서 가장 작은 값
    successor = root.right
    while successor.left:
        successor = successor.left
    root.val = successor.val  # 현재 노드 값을 후속자의 값으로 교체
    root.right = delete_node(root.right, successor.val)  # 중복된 후속자 노드를 제거
    return root
# 삭제
def delete_node(root, val):
    if root is None:
        return root
    if val < root.val:
        root.left = delete_node(root.left, val)
    elif val > root.val:
        root.right = delete_node(root.right, val)
    else:
        # 삭제할 노드를 찾음
        if root.left is None and root.right is None:
            return delete_leaf_node(root)  # 1. 리프 노드
        elif root.left is None or root.right is None:
            return delete_single_child_node(root)  # 2. 자식 1개
        else:
            return delete_two_children_node(root)  # 3. 자식 2개
    return root
# 중위 순회 (정렬된 출력 확인용)
def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.val, end=" ")
        inorder_traversal(root.right)
# ---------------- 테스트 ---------------- #
if __name__ == "__main__":
    root = None
    values = [50, 30, 70, 20, 40, 60, 80]
    for val in values:
        root = insert(root, val)
    print("중위 순회 (삽입 후):")
    inorder_traversal(root)
    print()
    root = delete_node(root, 20)  # 리프 노드 삭제
    root = delete_node(root, 30)  # 자식 1개
    root = delete_node(root, 50)  # 자식 2개
    print("중위 순회 (삭제 후):")
    inorder_traversal(root)
    print()