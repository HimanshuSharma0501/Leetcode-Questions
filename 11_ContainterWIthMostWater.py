class Solution:
    def maxArea(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        mA=0
        while l<r:
            cA=min(height[l],height[r])*(r-l)
            mA=max(mA,cA)
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return mA
        