def Solution(head):
    rev = None
    fast = slow = head

    while fast and fast.next:
        fast = fast.next.next
        rev, rev.next, slow = slow, rev, slow.next