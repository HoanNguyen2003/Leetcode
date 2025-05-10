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

    def middleNode(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow


data = [1, 2, 3, 4, 5]
run = Solution()
head = run.build_linked_list(data)
mid = run.middleNode(head)
print(mid.val)  

# Kết quả: 3
