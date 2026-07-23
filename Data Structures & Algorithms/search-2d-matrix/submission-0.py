class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        columns = len(matrix[0])

        top = 0
        bottom = rows - 1

        while top <= bottom:
            midRow = (top + bottom) // 2
            if target > matrix[midRow][-1]:
                top = midRow + 1
            elif target < matrix[midRow][0]:
                bottom = midRow - 1
            else:
                break
        
        if not (top <= bottom):
            return False
        
        binaryRow = (top + bottom) // 2
        left, right = 0, columns - 1
        while left <= right:
            mid = (left + right ) //2
            if target > matrix[binaryRow][mid]:
                left = mid + 1
            elif target < matrix[binaryRow][mid]:
                right = mid - 1
            else:
                return True
        return False
        