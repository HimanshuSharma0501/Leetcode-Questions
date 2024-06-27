class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ptr1=0
        if len(s)==0:
            return True
        for ptr2 in range(len(t)):
            if s[ptr1]==t[ptr2]:
                ptr1+=1
            if ptr1==len(s):
                return True
        return False