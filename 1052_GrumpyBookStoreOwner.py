class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        windowSum=0
        nonGrumpySum=0
        maxWindowSum=0
        for i in range(len(customers)):
            if grumpy[i]==0:
                nonGrumpySum+=customers[i]
            if i<minutes:
                windowSum+= customers[i] if grumpy[i]==1 else 0
            else:
                windowSum+=(customers[i] if grumpy[i]==1 else 0)-(customers[i-minutes] if grumpy[i-minutes]==1 else 0)
            maxWindowSum=max(maxWindowSum,windowSum)
        return nonGrumpySum+maxWindowSum