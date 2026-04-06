class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        import collections
        
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for row in range(9):
            for col in range(9):
                val = board[row][col]
                if val == '.':
                    continue

                if val in rows[row]:
                    return False
                if val in cols[col]:
                    return False
                if val in squares[(row//3, col//3)]:
                    return False

                rows[row].add(val)
                cols[col].add(val)
                squares[(row//3, col//3)].add(val)
        
        return True
   