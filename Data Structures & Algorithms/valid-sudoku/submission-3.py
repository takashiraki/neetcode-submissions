class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()
        for row in range(9):

            for column in range(9):

                val = board[row][column] 

                if val == ".":
                    continue

                row_key = (val, "row", row)
                column_key = (val, "col", column)
                box_key = (val, "box", row // 3, column // 3)

                if row_key in seen or column_key in seen or box_key in seen:
                    return False
                
                seen.add(row_key)
                seen.add(column_key)
                seen.add(box_key)

        return True