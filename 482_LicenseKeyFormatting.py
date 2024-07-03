class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s=s.replace('-',"").upper()
        firstpartLen=len(s)%k
        res=s[:firstpartLen]
        for i in range(firstpartLen,len(s),k):
            if res:
                res+="-"
            res+=s[i:i+k]
        return res