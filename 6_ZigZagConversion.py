class Solution:
    def convert(self, s: str, numRows: int) -> str:
        n=len(s)
        ans=[[] for _ in range(numRows)]
        i=0
        while i<n:
            j=0
            while i<n and j<numRows:
                ans[j].append(s[i])
                i+=1
                j+=1
            j-=2
            while i<n and j>0:
                ans[j].append(s[i])
                i+=1
                j-=1
        res=[]
        for row in range(numRows):
            res.append(''.join(ans[row]))
        return ''.join(res)
        
        
        