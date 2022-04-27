import sys

class Solution:
    def do(self, test_case, D, W, K, mat):
        # W = COLS, D = ROWS, K = Pass
        ROWS, COLS = D, W
        res = K
        chems = [[0] * COLS, [1] * COLS]

        if self.check(ROWS, COLS, mat, K) or K == 1:

            return f"#{test_case} 0"

        def backtrack(i, count, mat):
            nonlocal res
            if i == ROWS:
                if self.check(ROWS, COLS, mat, K):
                    res = min(res, count)

                return

            if count < res:
                for j in range(i, ROWS):
                    ogRow = mat[j]
                    for chem in chems:
                        mat[j] = chem
                        backtrack(j + 1, count + 1, mat)
                        mat[j] = ogRow
                        if count < res:
                            if self.check(ROWS, COLS, mat, K):
                                res = min(res, count)

        backtrack(0, 0, mat)
        return f"#{test_case} {res}"

    def check(self, rows, cols, mat, k):
        for c in range(cols):
            prv, count, complete = mat[0][c], k - 1, False
            for r in range(1, rows):
                if complete:
                    break

                if prv == mat[r][c]:
                    count -= 1
                    if count <= 0:
                        complete = True
                    continue

                count = k - 1
                prv = mat[r][c]

            if not complete:
                return False

        return True

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
