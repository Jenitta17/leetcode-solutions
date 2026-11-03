class Solution(object):
    def rotate(self, matrix):
        n = len(matrix)
        matrix.reverse()
        for i in range(n):
            for j in range(i + 1, n):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
        
