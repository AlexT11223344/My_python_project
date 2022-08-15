class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        first, second = head, head.next if head else None
        while second:
            if first.val == second.val:
                second = second.next
                first.next = second
            else:
                first = second
                second = second.next

        return head