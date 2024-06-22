class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        left=0
        odds=0
        res=0
        for right in range(len(nums)):
            if nums[right]%2!=0:
                odds+=1
            while odds>k:
                if nums[left]%2!=0:
                    odds-=1
                left+=1
            if odds==k:
                tempLeft=left
                while tempLeft<right and nums[tempLeft]%2==0:
                    res+=1
                    tempLeft+=1
                res+=1
        return res
        
            
            
        