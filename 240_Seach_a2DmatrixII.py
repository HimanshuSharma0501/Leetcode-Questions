class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        cols = len(matrix[0]) - 1
        h = cols
        for i in range(len(matrix)):
            l = 0
            while l <= h:
                m = (l + h) >> 1
                if matrix[i][m] == target:
                    return True
                elif matrix[i][m] < target:
                    l = m + 1
                else:
                    h = m - 1
            h = h + 1 if h < cols else cols
        return False