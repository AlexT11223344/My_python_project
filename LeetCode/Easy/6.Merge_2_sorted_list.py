# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        result = []
        for i in range(0, len(list1)):
            result.append(list1[i])
        for j in range(0, len(list2)):
            result.append(list2[j])
        result.sort()
        return result


list_1 = [1,2,4]
list_2 = [1,3,4,9,10]
sol = Solution()
result = sol.mergeTwoLists(list_1, list_2)
print(result)