# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        buckets = [[] for _ in range(19)] # 숫자별 저장공간
        for li in lists:
            cursor = li
            while cursor:
                buckets[0].append(cursor)
                cursor = cursor.next
        
        for power in range(5):
            temp = [[] for _ in range(19)]
            for bucket in buckets:
                for node in bucket:
                    sign = node.val >= 0
                    digit = (abs(node.val) % 10 ** (power + 1)) // (10 ** power)
                    if node.val >= 0:
                        digit += 9
                    else:
                        digit = 9 - digit
                    temp[digit].append(node)
            buckets = temp
        
        head = None
        tail = None
        for bucket in buckets:
            for node in bucket:
                if head is None:
                    head = node
                    tail = node
                else:
                    tail.next = node
                    tail = tail.next
                    
        return head