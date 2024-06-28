class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        deg=[0]*n
        for i,j in roads:
            deg[i]+=1
            deg[j]+=1
        deg.sort(reverse=True)
        ans=0
        for i,j in enumerate(deg):
            ans+=(n-i)*j
        return ans
        