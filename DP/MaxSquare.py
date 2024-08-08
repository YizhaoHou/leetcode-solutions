import math
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        dp = []
        for i in range(len(matrix)):
            dp.append([0 for j in range(len(matrix[0]))])
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == "1":
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        max_edge = int(math.sqrt(dp[i -1][j - 1]))
                        edge = 1 + self.detect_edge(max_edge, dp, i, j)
                        dp[i][j] = edge ** 2
        max_area = 0

        for subRow in dp:
            if max(subRow) > max_area:
                max_area = max(subRow)
        return max_area
    def detect_edge(self, edge_length, dp, i, j):
        return min(edge_length, int(math.sqrt(dp[i -1][j])), int(math.sqrt(dp[i][j - 1])))