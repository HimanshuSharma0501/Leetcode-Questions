class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        groups=time//(n-1)
        if groups%2==0:
            return (time%(n-1)+1)
        else:
            return (n-time%(n-1))            
        