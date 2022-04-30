import sys

class Solution:
    def do(self, T, N, W, H, mat):
        minBricks = float("inf")
        shoots = N
        ROWS, COLS = H, W
        def crush(mat, r, c):
            directions = ["U", "D", "R", "L"]
            q = [(r, c)]

            while q:
                curR, curC = q.pop(0)
                for d in directions:
                    for nxt in range(1, mat[curR][curC]):
                        if d == "U":
                            newR = curR - nxt
                            if newR >= 0:
                                if mat[newR][curC] != 0:
                                    q.append((newR, curC))

                            else: break

                        elif d == "D":
                            newR = curR + nxt
                            if newR < ROWS:
                                if mat[newR][curC] != 0:
                                    q.append((newR, curC))

                            else: break

                        elif d == "R":
                            newC = curC + nxt
                            if newC < COLS:
                                if mat[curR][newC] != 0:
                                    q.append((curR, newC))

                            else: break

                        else:
                            newC = curC - nxt
                            if newC >= 0:
                                if mat[curR][newC] != 0:
                                    q.append((curR, newC))

                            else: break

                mat[curR][curC] = 0

            return mat

        def pullDown(mat):
            for r in range(ROWS - 1, -1, -1):
                for c in range(COLS):
                    if mat[r][c] != 0:
                        for nxtR in range(ROWS - 1, r, -1):
                            if mat[nxtR][c] == 0:
                                mat[nxtR][c], mat[r][c] = mat[r][c], mat[nxtR][c]
                                break

            return mat

        def countBricks(mat):
            nonlocal minBricks

            tmpBricks = 0
            for r in range(ROWS):
                for c in range(COLS):
                    if mat[r][c] != 0:
                        tmpBricks += 1

            minBricks = min(minBricks, tmpBricks)

        def getHittable(mat):
            hittableBricks = []
            visited = set()
            for c in range(COLS):
                if mat[0][c] != 0:
                    visited.add(c)
                    hittableBricks.append((0, c))

            for r in range(1, ROWS):
                for c in range(COLS):
                    if mat[r][c] != 0:
                        if mat[r - 1][c] == 0 and c not in visited:
                            hittableBricks.append((r, c))
                            visited.add(c)

            return hittableBricks

        def dfs(mat, shots):
            if shoots > 0:
                hittableBricks = getHittable(mat)
                for r, c in hittableBricks:
                    newMat = [list(mat[r][:]) for r in range(ROWS)]
                    curMat = pullDown(crush(newMat, r, c))
                    countBricks(curMat)
                    dfs(curMat, shots - 1)

        dfs(mat, shots)

        return f"#{T} {minBricks}"

sys.stdin = open("mat_input.txt", "r")
T = int(input())
sol = Solution()
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N, W, H = map(int, input().split())
    mat = [list(map(int, input().split())) for _ in range(H)]

    print(sol.do(test_case, N, W, H, mat))

    # ///////////////////////////////////////////////////////////////////////////////////
