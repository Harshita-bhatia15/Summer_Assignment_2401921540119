class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
       n = len(mat)
       sum = 0
       for i in range(n):
            sum = sum + mat[i][i]
            sum = sum + mat[i][n-1-i]

       if n%2 != 0:
            sum = sum - mat[n//2][n//2]
        
       return sum
        