class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def build_linked_list(self, values):
        if not values:
            return None
        head = ListNode(values[0])
        curr = head
        for val in values[1:]:
            curr.next = ListNode(val)
            curr = curr.next
        return head
    
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        slow = fast = head
        while fast and fast.next:
            if fast == slow:
                return True
        return False
            

head = [3,2,0,-4] 
pos = 1
run = Solution()
head = run.build_linked_list(head)
print(run.hasCycle(head)) 

# Kết quả: True