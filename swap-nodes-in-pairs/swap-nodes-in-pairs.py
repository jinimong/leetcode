# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        cursor = head
        tail = dummy
        
        while cursor and cursor.next:
            right = cursor  # 변경 후 오른쪽으로
            left = cursor.next  # 변경 후 왼쪽으로
            
            cursor = cursor.next.next  # 커서 2칸 이동
            
            left.next = right
            right.next = cursor
            
            tail.next = left
            tail = tail.next.next
            
        return dummy.next