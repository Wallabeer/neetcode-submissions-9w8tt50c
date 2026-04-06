class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            seen = set()
            for element in row:
                if element == '.':
                    continue
                if element in seen:
                    return False
                else:
                    seen.add(element)
        
        for col in range(9):
            seen = set()
            for row in range(9):
                if board[row][col] == '.':
                    continue

                if board[row][col] in seen:
                    return False
                else:
                    seen.add(board[row][col])
        
        for boxRow in range(3):
            for boxCol in range(3):
                seen = set()
                for row in range(3):
                    for col in range(3):
                        if board[3*boxRow + row][3*boxCol + col] == '.':
                            continue
                        if board[3*boxRow + row][3*boxCol + col] in seen:
                            return False
                        else:
                            seen.add(board[3*boxRow + row][3*boxCol + col])

        return True
   