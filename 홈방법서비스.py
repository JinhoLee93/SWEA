import sys

class Solution:
    def do(self, test_case, M, mat):
        # M = cost per house
        ROWS, COLS = len(mat), len(mat[0])
        maxHouses = 0

        for r in range(ROWS):
            for c in range(COLS):
                k = 1
                while ((k - 1) <= len(mat)):
                    houses = 0
                    for newR in range(ROWS):
                        for newC in range(COLS):
                            distance = abs(newR - r) + abs(newC - c)
                            if distance <= (k - 1):
                                if mat[newR][newC] == 1:
                                    houses += 1

                    cost = k * k + ((k - 1) * (k - 1))
                    profit = houses * M
                    if (profit - cost) >= 0:
                        maxHouses = max(maxHouses, houses)

                    k += 1

        return f"#{test_case} {maxHouses}"

sys.stdin = open("security_input.txt", "r")
T = int(input())
sol = Solution()
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N, M = map(int, input().split())
    mat = [list(map(int, input().split())) for _ in range(N)]
    print(sol.do(test_case, M, mat))
    # ///////////////////////////////////////////////////////////////////////////////////
