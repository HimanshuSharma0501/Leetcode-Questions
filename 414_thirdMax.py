class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        lis = list(set(nums))
        lis.sort(reverse=True)
        l = len(lis)
        if l < 3:
            return lis[0]
        else:
            return lis[2]