import sys

class Solution:
    def do(self, test_case, N, mat):
        # N = ROWS, COLS
        ROWS, COLS = N, N
        dessert = set()
        directions = [(1, 1), (1, -1), (-1, -1), (-1, 1)]
        res = float("-inf")

        def dfs(r, c, origin, count, prvDir, started):
            nonlocal res

            if prvDir > len(directions) - 1:
                return

            r += directions[prvDir][0]
            c += directions[prvDir][1]

            if (r < 0 or c < 0 or
                r > ROWS - 1 or c > COLS - 1 or
                mat[r][c] in dessert):
                return

            if (r, c) == origin and started:
                res = max(res, count)
                return

            started = True
            dessert.add(mat[r][c])
            dfs(r, c, origin, count+1, prvDir, started)
            dfs(r, c, origin, count+1, prvDir+1, started)
            dessert.remove(mat[r][c])

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, (r, c), 1, 0, False)


        return f"#{test_case} {res}" if res != float("-inf") else f"#{test_case} {-1}"

sys.stdin = open("cafe_input.txt", "r")
T = int(input())
sol = Solution()
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N = list(map(int,input().split()))[0]
    mat = [list(map(int, input().split())) for _ in range(N)]
    print(sol.do(test_case, N, mat))
    # ///////////////////////////////////////////////////////////////////////////////////
