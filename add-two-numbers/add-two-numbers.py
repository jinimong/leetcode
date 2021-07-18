# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = ListNode()
        passed_value = 0
        c1 = l1
        c2 = l2
        node = result
        
        while True:
            v1 = 0
            if c1:
                v1 = c1.val
                if c1.next:
                    c1 = c1.next
                else:
                    c1 = None
                    
            v2 = 0
            if c2:
                v2 = c2.val
                if c2.next:
                    c2 = c2.next
                else:
                    c2 = None
                    
            val = v1 + v2 + passed_value
            node.val = val % 10
            passed_value = val // 10
            
            if c1 is None and c2 is None and passed_value == 0:
                break
            else:
                node.next = ListNode()
                node = node.next
                
        return result