class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        left = 0
        right = (m * n) - 1
        print(m, n)
        while left <= right:
            mid = (left + right) // 2
            midRow = mid // n
            midCol = mid % n
            # print(m, n)
            print(left, right)
            print(mid , midRow, midCol)
            
            val = matrix[midRow][midCol] 
            print(val)
            if val == target:
                return True
            
            if val > target:
                right = mid - 1
            else:
                left = mid + 1
            
        return False