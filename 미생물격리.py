import sys

class Solution:
    def do(self, test_case, N, M, microbes):
        # N = ROWS, COLS, M = Time quarantined
        # microbes = [r, c, num, dir]
        ROWS, COLS = N, N
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] # Up, Down, Left, Right
        map = {(r, c): [(num, d)] for r, c, num, d in microbes}
        boundary = set()
        res = 0

        for r in range(ROWS):
            for c in range(COLS):
                if (r == 0 or c == 0 or
                    r == ROWS - 1 or c == COLS - 1):
                    boundary.add((r, c))

        for _ in range(M):
            tmp = list(map.keys())
            collisions = set()
            for r, c in tmp:
                num, d = map[(r, c)][0][0], map[(r, c)][0][1]
                newR, newC = directions[d - 1]
                nxtR, nxtC = r + newR, c + newC

                if (nxtR, nxtC) in boundary:
                    if d % 2 == 0:
                        d -= 1
                    else:
                        d += 1
                    num //= 2

                if (nxtR, nxtC) not in map:
                    map[(nxtR, nxtC)] = [(num, d)]

                else:
                    map[(nxtR, nxtC)].append((num, d))
                    collisions.add((nxtR, nxtC))

                if len(map[(r, c)]) == 1:
                    map.pop((r, c))

                else:
                    map[(r, c)].pop(0)

            for collision in collisions:
                newNum, newD, maxNum = 0, 0, float("-inf")
                for num, d in map[collision]:
                    newNum += num
                    if num > maxNum:
                        maxNum = num
                        newD = d

                map[collision] = [(newNum, newD)]

        for key in map.keys():
            res += map[key][0][0]

        return f"#{test_case} {res}"

sys.stdin = open("microbe_input.txt", "r")
T = int(input())
sol = Solution()
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N, M, K = map(int, input().split())
    microbes = [list(map(int, input().split())) for _ in range(K)]
    print(sol.do(test_case, N, M, microbes))
    # ///////////////////////////////////////////////////////////////////////////////////
