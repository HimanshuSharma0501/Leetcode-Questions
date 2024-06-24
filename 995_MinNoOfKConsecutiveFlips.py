class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        n=len(nums)
        ans=0
        #time limit exceeded
        # for i in range(n):
        #     if nums[i]==0:
        #         if i+k>n:
        #             return -1
        #         nums[i:i+k]=[num^1 for num in nums[i:i+k]]
        #         ans+=1
        hasEverFlipped=[0]*n
        validFlipCountCurrentIdx=0
        for i in range(n):
            if i>=k:
                if hasEverFlipped[i-k]:
                    validFlipCountCurrentIdx-=1
            if validFlipCountCurrentIdx%2==nums[i]:
                if i+k>n:
                    return -1

                validFlipCountCurrentIdx+=1
                hasEverFlipped[i]=1
                ans+=1
        return ans
        