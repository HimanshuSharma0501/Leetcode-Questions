class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_sum=curr=sum(nums[:k])
        for i in range(len(nums)-k):
            curr=curr-nums[i]+nums[i+k]
            if curr>max_sum:
                max_sum=curr
        return max_sum/k