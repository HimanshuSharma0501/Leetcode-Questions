
class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        rows=[]
        cols=[]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    rows.append(i)
                    cols.append(j)
        rows=list(set(rows))
        cols=list(set(cols))
        minr=min(rows)
        maxr=max(rows)
        minc=min(cols)
        maxc=max(cols)
        area=(maxr-minr+1)*(maxc-minc+1)
        return area