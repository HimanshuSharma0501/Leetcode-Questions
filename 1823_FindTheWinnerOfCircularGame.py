class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        circle=[num for num in range(1,n+1)]
        idx=0
        while len(circle)!=1:
            nRem=(idx+k-1)%len(circle)
            circle.pop(nRem)
            idx=nRem
        return circle[0]
        