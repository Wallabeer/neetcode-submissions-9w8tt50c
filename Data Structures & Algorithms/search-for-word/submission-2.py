class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(word)
        
        rows = len(board)
        cols = len(board[0])
        
        def helper(row, col, i):
            if i == n:
                return True

            if row >= rows or row < 0:
                return
            if col >= cols or col < 0:
                return
            
            if (row, col) in path:
                return

            if board[row][col] != word[i]:
                return

            path.add((row, col))
            
            result = (
                        helper(row+1, col, i+1)
                        or helper(row-1, col, i+1)
                        or helper(row, col+1, i+1)
                        or helper(row, col-1, i+1)
                    )
            if result:
                return True
            else:
                path.remove((row, col))
                return result
            
        
        for row in range(rows):
            for col in range(cols):
                path = set()
                if helper(row,col,0):
                    return True
        return False
            
