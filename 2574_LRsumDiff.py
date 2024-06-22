class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        ls=0
        rs=sum(nums)
        ans=[]
        for x in nums:
            ls+=x
            ans.append(abs(ls-rs))
            rs-=x
        return ans

        