import sys

class Solution:
    def __init__(self):
        self.runway = 0

    def do(self, T, N, X, mat):
        rowMat = [mat[r][:] for r in range(N)]
        colMat = [[mat[r][c] for r in range(N)] for c in range(N)]

        for n in range(N):
            self.check(rowMat[n], X)

        for n in range(N):
            self.check(colMat[n], X)

        return f"#{T} {self.runway}"

    def check(self, arr, L):
        X = L
        idx = len(arr)
        prvHeight, length, complete, putRamp = arr[0], 1, True, False
        for i in range(1, idx):
            curHeight = arr[i]
            diff = abs(prvHeight - curHeight)
            if diff == 0:
                length += 1

            elif diff > 1:
                complete = False
                break

            else:
                if prvHeight > curHeight:
                    if putRamp:
                        if length < L:
                            complete = False
                            break
                        else:
                            putRamp = False

                    length = 1
                    putRamp = True

                elif prvHeight < curHeight:
                    if length < L:
                        complete = False
                        break

                    length = 1

            if length == L and putRamp:
                length = 0
                putRamp = False

            prvHeight = curHeight

            if i == idx - 1:
                if putRamp:
                    if length < L:
                        complete = False
                        break

        if complete:
            self.runway += 1

sys.stdin = open("runway_input.txt", "r")
T = int(input())
sol = Solution()
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N, X = map(int, input().split())
    mat = [list(map(int, input().split())) for _ in range(N)]
    print(sol.do(test_case, N, X, mat))
    sol.runway = 0
    # ///////////////////////////////////////////////////////////////////////////////////
