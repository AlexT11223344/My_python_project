class Solution:
    def searchInsert(self, nums, target):

        if len(nums) == 1:
            if nums[0] < target:
                return 1
            elif nums[0] > target:
                return 0
            else:
                return 0
        else:
            mid_point = int(len(nums) / 2)
            count = 0
            if nums[mid_point] == target:
                return mid_point

            elif nums[mid_point] < target:
                for i in range(mid_point, len(nums)):
                    if nums[i] >= target:
                        return i
                    else:
                        count += 1
                        continue
                if count != 0:
                    return len(nums)

            else:
                for j in range(0, mid_point + 1):
                    if nums[j] >= target:
                        return j
                    else:
                        count += 1
                if count != 0:
                    return mid_point - 1