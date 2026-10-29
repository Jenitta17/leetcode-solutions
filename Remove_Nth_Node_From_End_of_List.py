class Solution(object):
    def removeNthFromEnd(self, head, n):
        length = 0
        node = head
        while node:
            length += 1
            node = node.next

        dummy = ListNode(0, head)
        node = dummy
        for _ in range(length - n):
            node = node.next

        node.next = node.next.next
        return dummy.next
