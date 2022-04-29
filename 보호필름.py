import sys

class Solution:
    def do(self, test_case, D, W, K, mat):
        # D = ROWS, W = COLS, K = pass
        ROWS, COLS = D, W
        def checkFilm(mat):
            for c in range(COLS):
                prv, tmpK, complete = mat[0][c], K - 1, False
                for r in range(1, ROWS):
                    if complete:
                        break
                    if mat[r][c] == prv:
                        tmpK -= 1
                        if tmpK <= 0:
                            complete = True
                        continue
                    tmpK = K - 1
                    prv = mat[r][c]
                if not complete:
                    return False
            return True

        if K == 1 or checkFilm(mat):
            return f"#{test_case} {0}"
        chems = [[0] * COLS, [1] * COLS] # A, B
        res = K
        def dfs(r, count):
            nonlocal res
            if r == ROWS and count < res:
                if checkFilm(mat):
                    res = min(res, count)
                return
            elif count < res:
                for newR in range(r, ROWS):
                    ogRow = mat[newR]
                    for chem in chems:
                        if checkFilm(mat) and count < res:
                            res = min(res, count)
                            return
                        mat[newR] = chem
                        dfs(newR + 1, count + 1)
                        mat[newR] = ogRow

        dfs(0, 0)
        return f"#{test_case} {res}"

sys.stdin = open("film_input.txt", "r")
T = int(input())
sol = Solution()
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    D, W, K = map(int, input().split())
    mat = [list(map(int, input().split())) for _ in range(D)]
    print(sol.do(test_case, D, W, K, mat))
    # ///////////////////////////////////////////////////////////////////////////////////
