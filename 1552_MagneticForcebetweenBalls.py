class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        
        low=1
        high=position[-1]-position[0]
        while low<=high:
            mid=(low+high)//2
            bPlaced=1
            prevPos=position[0]
            for i in range(1,len(position)):
                if position[i]-prevPos>=mid:
                    bPlaced+=1
                    prevPos=position[i]
            if bPlaced>=m:
                low=mid+1
                hForce=mid
            else:
                high=mid-1
        return hForce

