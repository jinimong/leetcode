class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        left = l1
        right = l2
        head = None
        cursor = None

        while left or right:
            
            if right is None:
                target = left
                left = left.next
            elif left is None:
                target = right
                right = right.next
            elif left.val < right.val:
                target = left
                left = left.next
            else:
                target = right
                right = right.next

            if cursor is None:
                cursor = target
                head = target
            else:
                cursor.next = target
                cursor = cursor.next

        return head