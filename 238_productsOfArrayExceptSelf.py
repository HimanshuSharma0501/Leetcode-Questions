class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        product=1
        flag=True
        ans=[]
        cnt=0
        for i in nums:
            if i==0:
                cnt+=1
                continue
                
            else:
                flag=False
                
        if flag==True or cnt>1:
            return [0]*len(nums)
        flag=True             



        for i in nums:
            if i==0:
                flag=False

            if i is not 0:
                product*=i
        if flag==True:
            for i in nums:
                ans.append(product/i)
        else:
            ans=[0]*(len(nums))
            for i in range(len(nums)):
                if nums[i]==0:
                    ans[i]=product
        return ans            


                
