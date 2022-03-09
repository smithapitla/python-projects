# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        nums = [2,7,11,15]
        target = 9
        nums_map = {}
        for i in range (0, len(nums)):
            nums_map[nums[i]] = i

        for i in range (0, len(nums)):
            x = target - nums[i]
            if(x in nums_map):
                return [i, nums_map[x]]
        return nums_map
        
