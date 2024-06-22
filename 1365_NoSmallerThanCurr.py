class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        num=sorted(nums)
        res=[]
        for i in nums:
            res.append(num.index(i))
        return res