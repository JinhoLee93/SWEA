import sys

class Solution:
    def do(self, test_case, N, M, R, C, L, mat):
        # N = ROWS, M = COLS, (R, C) = Coordinate, L = time spent
        ROWS, COLS = N, M
        pipes = [[(-1, 0), (1, 0), (0, -1), (0, 1)], [(-1, 0), (1, 0)], [(0, -1), (0, 1)],
                 [(-1, 0), (0, 1)], [(1, 0), (0, 1)], [(1, 0), (0, -1)], [(-1, 0), (0, -1)]]
        visited = set()
        visitedMap = set()

        def isConnected(curR, curC, prvR, prvC):
            curPipe = mat[curR][curC] - 1

            for newR, newC in pipes[curPipe]:
                if (curR + newR, curC + newC) == (prvR, prvC):
                    return True

            return False

        def dfs(r, c, count, prvR, prvC):
            if (r < 0 or c < 0 or
                r > ROWS - 1 or c > COLS - 1 or
                (r, c) in visited or
                mat[r][c] == 0 or
                count == L):
                return

            if prvR != -1 and prvC != -1:
                if not isConnected(r, c, prvR, prvC):
                    return

            visitedMap.add((r, c))

            pipe = mat[r][c] - 1
            for newR, newC in pipes[pipe]:
                visited.add((r, c))
                dfs(r + newR, c + newC, count + 1, r, c)
                visited.remove((r, c))

        dfs(R, C, 0, -1, -1)
        return f"#{test_case} {len(visitedMap)}"

sys.stdin = open("jail_input.txt", "r")
T = int(input())
sol = Solution()
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N, M, R, C, L = map(int, input().split())
    mat = [list(map(int, input().split())) for _ in range(N)]
    print(sol.do(test_case, N, M, R, C, L, mat))
    # ///////////////////////////////////////////////////////////////////////////////////
