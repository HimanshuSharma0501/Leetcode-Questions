class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        a=0
        b=0
        for i in nums:
            if i%3==1:
                a+=1
            elif i%3==2:
                b+=1
        return a+b