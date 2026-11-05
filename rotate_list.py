class Solution(object):
    def rotateRight(self, head, k):
        if head is None:
            return head
        length = 0
        node = head
        while node is not None:
            length = length + 1
            node = node.next
        k = k % length
        if k == 0:
            return head
        steps = length - k
        first_end = head
        for i in range(steps - 1):
            first_end = first_end.next
        second_start = first_end.next
        first_end.next = None
        node = second_start
        while node.next is not None:
            node = node.next
        node.next = head
        return second_start
