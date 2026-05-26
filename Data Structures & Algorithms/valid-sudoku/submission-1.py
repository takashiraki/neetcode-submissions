class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()

        for row in range(9):
            for colum in range(9):
                val = board[row][colum]

                if val == ".":
                    continue

                row_key =  (val, "row", row)
                col_key = (val, "col", colum)
                box_key = (val, "box", row // 3, colum // 3)

                if row_key in seen or col_key in seen or box_key in seen:
                    return False
                
                seen.add(row_key)
                seen.add(col_key)
                seen.add(box_key)
        
        return True