class Solution:
    def do(self, T, N, mat):
        # N = Number of Atoms, mat = x, y, move, K(energy)
        directions = [(0, 0.5), (0, -0.5), (-0.5, 0), (0.5, 0)] # UP, DOWN, LEFT, RIGHT
        res = 0
        map = dict()
        collisions = {}
        for n in range(N):
            map[(mat[n][2], mat[n][3], n)] = (mat[n][0], mat[n][1])

        # Setting up the time table
        while len(map) >= 2:
            tmp = list(map.keys())
            collisions, idxSet = {}, set()
            for direction, energy, ID in tmp:
                x, y = map[(direction, energy, ID)]
                if x > 1000 or x < -1000 or y > 1000 or y < -1000:
                    map.pop((direction, energy, ID))
                    continue

                newX, newY = directions[direction]
                nxtX, nxtY = x + newX, y + newY
                map[(direction, energy, ID)] = (nxtX, nxtY)

                # Collision Check
                coordinate = map[(direction, energy, ID)]
                if coordinate not in collisions:
                    collisions[coordinate] = [(direction, energy, ID)]
                else:
                    collisions[coordinate].append((direction, energy, ID))
                    idxSet.add(coordinate)

            for idx in idxSet:
                for popDir, energyGone, ID in collisions[idx]:
                    res += energyGone
                    map.pop((popDir, energyGone, ID))

        return f"#{T} {res}"

sys.stdin = open("atom_input.txt", "r")
T = int(input())
sol = Solution()
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N = int(input().split()[0])
    mat = [list(map(int, input().split())) for _ in range(N)]
    print(sol.do(test_case, N, mat))
    # ///////////////////////////////////////////////////////////////////////////////////
