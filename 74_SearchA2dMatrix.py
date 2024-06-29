class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        r, c = len(matrix), len(matrix[0])
        left, right = 0, r * c - 1

        while left <= right:
            mid = (left + right) // 2
            mid_row, mid_col = divmod(mid, c)

            if matrix[mid_row][mid_col] == target:
                return True
            elif matrix[mid_row][mid_col] < target:
                left = mid + 1
            else:
                right = mid - 1

        return False