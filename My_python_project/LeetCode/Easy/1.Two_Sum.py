class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        _x = 0
        for i in range(0,len(nums)):
            for j in range(_x + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return i, j
                else:
                    continue
            _x += 1