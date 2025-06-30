class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m, n = len(img), len(img[0])
        result = [[0] * n for _ in range(m)]
    
        for i in range(m):
            for j in range(n):
                total = 0
                count = 0
                for ni in range(i - 1, i + 2):
                    for nj in range(j - 1, j + 2):
                        if 0 <= ni < m and 0 <= nj < n:
                            total += img[ni][nj]
                            count += 1
                result[i][j] = total // count  # floor
        return result