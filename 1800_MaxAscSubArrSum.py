class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        sums = []
        current = nums[0]
        if len(nums) == 1:
            return(nums[0])
        else:
            for i in range(len(nums)):
                if i == (len(nums)-1):
                    if nums[i-1] < nums[i]:
                        sums = sums + [current]
                        
                elif nums[i] < nums[i+1]:
                    current = current + nums[i+1]
                else:
                    sums = sums + [current]
                    current = nums[i+1]
            return(max(sums))