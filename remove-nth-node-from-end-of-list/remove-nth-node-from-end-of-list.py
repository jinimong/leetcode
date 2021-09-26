from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getSize(self, head: Optional[ListNode]):
        size = 0
        current = head

        while current:
            size += 1
            current = current.next

        return size

    def removeNthFromEnd(
        self, head: Optional[ListNode], n: int
    ) -> Optional[ListNode]:

        target_idx = self.getSize(head) - n

        idx = 0
        prev = None
        current = head
        result = head

        while current:
            if idx == target_idx:
                delete_target = current
                if prev:
                    prev.next = delete_target.next if delete_target else None
                else:
                    result = delete_target.next
                del delete_target
                break

            idx += 1
            prev = current
            current = current.next

        return result