class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        averages=[]
        nums.sort()
        while nums:
            min=nums.pop(0)
            max=nums.pop(-1)
            avg=(min+max)/2
            averages.append(avg)
        averages.sort()
        return averages[0]