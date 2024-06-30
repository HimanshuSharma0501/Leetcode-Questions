class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        par = [i for i in range(n+1)]
        def find(x):
            res = x
            while par[res] != res:
                par[res] = par[par[res]]
                res = par[res]
            return res

        def union(x,y):
            p1,p2  = find(x),find(y)
            if p1 != p2:
                par[p2] = p1
                return True
            else:
                return False

        common = []
        alice = []
        bob = []
        for t,x,y in edges:
            if t == 3:
                common.append((x,y))
            elif t == 2:
                bob.append((x,y))
            else:
                alice.append((x,y))
        count = 0
        com_edges = 0
        for x,y in common:
            u = union(x,y)
            if not u:
                count+=1
            else:
                com_edges +=1
        temp = par.copy()
        al_edges = com_edges
        for x,y in alice:
            u = union(x,y)
            if not u:
                count+=1
            else:
                al_edges+=1
        
        par = temp
        bob_edges = com_edges
        for x,y in bob:
            u = union(x,y)
            if not u:
                count+=1
            else:
                bob_edges += 1
        return count if al_edges == bob_edges == n-1 else -1