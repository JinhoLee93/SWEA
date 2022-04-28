import sys
class Solution:
    def do(self, test_case, N, K, mat):
        # ROWS = COLS = N, K = Depth
        ROWS = COLS = N
        highestHeight = 0
        highestPeaks = set()
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        res = 0
        visited = set()

        for r in range(ROWS):
            for c in range(COLS):
                highestHeight = max(highestHeight, mat[r][c])

        for r in range(ROWS):
            for c in range(COLS):
                if mat[r][c] == highestHeight:
                    highestPeaks.add((r, c))

        def dfs(r, c, prv, count, chance):
            nonlocal res
            if (r < 0 or c < 0 or
                r > ROWS - 1 or c > COLS - 1 or
                (r, c) in visited or
                mat[r][c] == 0):
                res = max(res, count)
                return

            if mat[r][c] >= prv and prv >= 0:
                if chance == 0:
                    if mat[r][c] - K >= prv:
                        res = max(res, count)
                        return

                    else:
                        prv = max(mat[r][c] - K, prv - 1)
                        chance += 1

                elif chance == 1:
                    res = max(res, count)
                    return

            else:
                prv = mat[r][c]

            if prv == -1:
                prv = mat[r][c]

            for newR, newC in directions:
                visited.add((r, c))
                dfs(r + newR, c + newC, prv, count+1, chance)
                visited.remove((r, c))

        for r, c in highestPeaks:
            dfs(r, c, -1, 0, 0)

        return f"#{test_case} {res}"

sys.stdin = open("hiking_input.txt", "r")
T = int(input())
sol = Solution()
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N, K = map(int, input().split())
    mat = [list(map(int, input().split())) for _ in range(N)]
    print(sol.do(test_case, N, K, mat))
    # ///////////////////////////////////////////////////////////////////////////////////
