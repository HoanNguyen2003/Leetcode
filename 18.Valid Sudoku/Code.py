class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rows = {}
        cols = {}
        boxes = {}

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == '.':
                    continue

                box_key = (i // 3, j // 3)

                if i not in rows:
                    rows[i] = set()
                if j not in cols:
                    cols[j] = set()
                if box_key not in boxes:
                    boxes[box_key] = set()

                if num in rows[i] or num in cols[j] or num in boxes[box_key]:
                    return False

                rows[i].add(num)
                cols[j].add(num)
                boxes[box_key].add(num)

        return True

# Input: board = 
# [["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: true