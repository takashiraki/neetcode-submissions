import bisect

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for r_index, row in enumerate(matrix):
            print("r_index: ",r_index)
            print("raw: ",row)
            idx = bisect.bisect_left(row,target)
            print("idx:", idx)

            if idx < len(row) and row[idx] == target:
                return True
            
        return False