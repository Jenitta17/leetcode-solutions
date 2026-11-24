class Solution(object):
    def partition(self, head, x):
        small_dummy = ListNode(0)
        big_dummy = ListNode(0)
        small = small_dummy
        big = big_dummy
        current = head
        while current is not None:
            if current.val < x:
                small.next = current
                small = small.next
            else:
                big.next = current
                big = big.next
            current = current.next
        big.next = None
        small.next = big_dummy.next
        return small_dummy.next
