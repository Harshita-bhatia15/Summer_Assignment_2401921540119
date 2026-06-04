class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return []

        res = []
        top =0
        left = 0
        bottom = len(matrix) - 1
        right = len(matrix[0]) - 1

        while (left<=right and top<=bottom):
            for i in range(left, right+1):
                res.append(matrix[top][i])
            top = top+1
            
            for i in range(top, bottom+1):
                res.append(matrix[i][right])
            right = right-1

            if top<=bottom:
                for i in range(right, left-1, -1):
                    res.append(matrix[bottom][i])
                bottom = bottom-1
            
            if left<=right:
                for i in range(bottom, top-1, -1):
                    res.append(matrix[i][left])
                left = left+1
        return res
