import sys

class Solution:
    def do(self, T, N, M, K, mat):
        # N = ROWS, M = COLS, K = Time
        ROWS, COLS, TIME = N, M, K
        map = {}

        for r in range(ROWS):
            for c in range(COLS):
                if mat[r][c] != 0:
                    map[(r, c)] = [mat[r][c], mat[r][c]] # time left, life


        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        q = [(r, c) for (r, c) in map.keys()]
        onLimbo = {}
        doneFor = []

        for _ in range(K):
            tmp = q.copy()

            # Cells that expired
            aboutToAdd = {}
            for curR, curC in doneFor:
                for newR, newC in directions:
                    nxtR, nxtC = curR + newR, curC + newC
                    if (nxtR, nxtC) not in map:
                        aboutToAdd[(nxtR, nxtC)] = [max(aboutToAdd.get((nxtR, nxtC), (0, 0))[1], map[(curR, curC)][1]),
                                                    max(aboutToAdd.get((nxtR, nxtC), (0, 0))[1], map[(curR, curC)][1])]

            for key, val in aboutToAdd.items():
                map[key] = val
                q.append(key)

            doneFor = []

            # Dead but Alive
            keys = list(onLimbo.keys())
            for key in keys:
                onLimbo[key] -= 1
                if onLimbo[key] == 0:
                    onLimbo.pop(key)

            # Degenerating Cells
            for _ in range(len(tmp)):
                oldR, oldC = q.pop(0)
                map[(oldR, oldC)][0] -= 1
                if map[(oldR, oldC)][0] > 0:
                    q.append((oldR, oldC))

                # Active
                elif map[(oldR, oldC)][0] == 0:
                    doneFor.append((oldR, oldC))
                    onLimbo[(oldR, oldC)] = map[(oldR, oldC)][1]

        resSet = set(doneFor + q + list(onLimbo.keys()))

        return f"#{T} {len(resSet)}"

sys.stdin = open("stemcell_input.txt", "r")
T = int(input())
sol = Solution()
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N, M, K = map(int, input().split())
    mat = [list(map(int, input().split())) for _ in range(N)]
    print(sol.do(test_case, N, M, K, mat))
    # ///////////////////////////////////////////////////////////////////////////////////
