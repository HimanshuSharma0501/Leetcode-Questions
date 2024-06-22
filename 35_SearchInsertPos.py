class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        s, e = 0, len(nums) - 1
        if nums[e] < target:
            return e + 1
        while s <= e:
            m = s + (e - s) // 2
            if nums[m] == target:
                return m
            if nums[m] > target:
                e = m - 1
            else:
                s = m + 1
        if target > nums[m] and target < nums[m + 1]:
            return m + 1
        else:
            return m