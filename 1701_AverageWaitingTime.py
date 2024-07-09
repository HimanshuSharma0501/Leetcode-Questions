class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        availabilityTime=0
        totalWait=0
        for arrival,timeNeeded in customers:
            availabilityTime=max(availabilityTime,arrival)+timeNeeded
            totalWait+=availabilityTime-arrival
        return totalWait/len(customers) 