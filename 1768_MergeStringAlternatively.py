class Solution(object):
    def mergeAlternately(self, word1, word2):
        
        res=""
        n=min(len(word1),len(word2))
        for i in range(n):
            res+=word1[i]+word2[i]
        if len(word1)>len(word2):
            res+=word1[n:]
        else:
            res+=word2[n:]
        return res