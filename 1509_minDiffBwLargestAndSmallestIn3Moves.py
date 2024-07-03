class Solution:
    def minDifference(self, nums: List[int]) -> int:
        left , right = 0, len(nums) - 4
        res=[]
        temp = 0
        nums.sort()
        if len(nums)<=4:
            return 0
        else:
            while(right < len(nums)):
                temp = nums[right] - nums[left]
                res.append(temp)
                left += 1
                right += 1
            return min(res)
        