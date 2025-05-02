# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]


class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        result = []
        top, bottom = 0, len(matrix) -1
        left, right = 0, len(matrix[0]) -1

        while top <= bottom and left <= right:
            # left to right
            for col in range(left, right + 1):
                result.append(matrix[top][col])
            top += 1

            # top to bottom
            for row in range(top, bottom + 1):
                result.append(matrix[row][right])
            right -= 1

            # right to left
            if top <= bottom:
                for col in range(right, left -1, -1):
                    result.append(matrix[bottom][col])
            bottom -= 1

            if left <= right:
                for row in range(bottom, top - 1, -1):
                    result.append(matrix[row][left])
            left += 1
        
        return result
        

matrix = [[1,2,3],[4,5,6],[7,8,9]]
run = Solution()
print(run.spiralOrder(matrix))