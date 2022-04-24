import sys

class Solution:
    def do(self, T, N, X, mat):
        ROWS, COLS = N, N
        L = X
        runway = 0

        for r in range(ROWS):
            prvHeight, length, complete, putRamp = mat[r][0], 1, True, False
            for c in range(1, COLS):
                curHeight = mat[r][c]
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

                if c == COLS - 1:
                    if putRamp:
                        if length < L:
                            complete = False
                            break

            if complete:
                runway += 1

        for c in range(COLS):
            prvHeight, length, complete, putRamp = mat[0][c], 1, True, False
            for r in range(1, ROWS):
                curHeight = mat[r][c]
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

                if r == ROWS - 1:
                    if putRamp:
                        if length < L:
                            complete = False
                            break

            if complete:
                runway += 1

        return f"#{T} {runway}"

sys.stdin = open("runway_input.txt", "r")
T = int(input())
sol = Solution()
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N, X = map(int, input().split())
    mat = [list(map(int, input().split())) for _ in range(N)]
    print(sol.do(test_case, N, X, mat))
    # ///////////////////////////////////////////////////////////////////////////////////
