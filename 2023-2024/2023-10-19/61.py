# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        for _ in range(k):
            current = head

            # Stop when current.next.next is None
            # Stop when the node two after the current is None
            while current.next.next is not None:
                current = current.next

            second_to_last = current
            last = current.next
            last.next = head
            head = last
            second_to_last.next = None

        return head
