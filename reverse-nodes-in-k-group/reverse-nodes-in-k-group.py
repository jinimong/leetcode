# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:
            return head

        stack = []
        dummy = ListNode()
        dummy.next = head
        tail = dummy
        cursor = head

        while cursor:
            stack.append(cursor)

            if len(stack) == k:
                prev_node_next = None
                prev_cursor_next = cursor.next

                for node in stack[::-1]:
                    if prev_node_next:
                        node.next = prev_node_next
                    prev_node_next = node.next
                    node.next = None
                    tail.next = node
                    tail = tail.next
                stack = []

                if prev_cursor_next is None:
                    break
                elif prev_node_next:
                    cursor = prev_node_next
            else:
                cursor = cursor.next

        if stack:
            tail.next = stack[0]

        return dummy.next