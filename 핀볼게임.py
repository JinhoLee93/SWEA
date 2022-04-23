import sys

class Solution:
    def do(self, T, N, mat):
        # N = ROWS, COLS, mat = Matrix
        ROWS, COLS = N, N
        maxScore = 0
        obstacles = {i for i in range(1, 6)}
        wormholes = {}
        blackholes = {}
        for r in range(ROWS):
            for c in range(COLS):
                if 6 <= mat[r][c] <= 10:
                    wormholes[(r, c)] = mat[r][c]

                elif mat[r][c] == -1:
                    blackholes[(r, c)] = -1

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)] # Down, Up, Right, Left
        q = []
        for r in range(ROWS):
            for c in range(COLS):
                if mat[r][c] == 0:
                    q.append((-1, -1, r, c, (-1, -1), 0, (-1, -1), False))
                    while q:
                        prvR, prvC, curR, curC, direction, score, startingPoint, wormholePassed = q.pop(0)
                        # Return or Black hole
                        if (curR, curC) == startingPoint or (curR, curC) in blackholes:
                            maxScore = max(maxScore, score)

                        else:
                            # Start
                            if startingPoint == (-1, -1):
                                for i in range(len(directions)):
                                    q.append((curR, curC, curR + directions[i][0], curC + directions[i][1], directions[i], score,
                                        (curR, curC), False))

                            # Logic
                            else:
                                if (curR < 0 or curR > ROWS - 1 or
                                        curC < 0 or curC > COLS - 1):
                                    # When the ball hits the top and bottom walls
                                    if (curR < 0 or curR > ROWS - 1):
                                        # Top wall
                                        if curR < 0:
                                            q.append((curR, curC, curR + directions[0][0], curC + directions[0][1], directions[0],
                                                score + 1, startingPoint, False))

                                        # Bottom wall
                                        else:
                                            q.append((curR, curC, curR + directions[1][0], curC + directions[1][1], directions[1],
                                                score + 1, startingPoint, False))

                                    # When the ball hits the leftmost and rightmost walls
                                    elif (curC < 0 or curC > COLS - 1):
                                        # Left wall
                                        if curC < 0:
                                            q.append((curR, curC, curR + directions[2][0], curC + directions[2][1], directions[2],
                                                score + 1,
                                                startingPoint, False))

                                        # Right wall
                                        else:
                                            q.append((curR, curC, curR + directions[3][0], curC + directions[3][1], directions[3],
                                                score + 1,
                                                startingPoint, False))

                                else:
                                    # If the ball is in empty space
                                    if mat[curR][curC] == 0:
                                        q.append((curR, curC, curR + direction[0], curC + direction[1], direction, score,
                                            startingPoint, False))

                                    # If the ball hits an obstacle
                                    elif mat[curR][curC] in obstacles:
                                        # Square
                                        if mat[curR][curC] == 5:
                                            # approached from bottom
                                            if curR == prvR - 1:
                                                q.append((curR, curC, curR + directions[0][0], curC + directions[0][1],
                                                    directions[0], score + 1, startingPoint, False))

                                            # approached from top
                                            elif curR == prvR + 1:
                                                q.append((curR, curC, curR + directions[1][0], curC + directions[1][1],
                                                    directions[1], score + 1, startingPoint, False))

                                            # approached from right
                                            elif curC == prvC - 1:
                                                q.append((curR, curC, curR + directions[2][0], curC + directions[2][1],
                                                    directions[2], score + 1, startingPoint, False))

                                            # approached from left
                                            elif curC == prvC + 1:
                                                q.append((curR, curC, curR + directions[3][0], curC + directions[3][1],
                                                    directions[3], score + 1, startingPoint, False))

                                        # Triangle 1
                                        elif mat[curR][curC] == 1:
                                            # (90 degree turn)
                                            # approached from top
                                            if curR == prvR + 1:
                                                q.append((curR, curC, curR + directions[2][0], curC + directions[2][1],
                                                    directions[2], score + 1, startingPoint, False))

                                            # approached from right
                                            elif curC == prvC - 1:
                                                q.append((curR, curC, curR + directions[1][0], curC + directions[1][1],
                                                    directions[1], score + 1, startingPoint, False))

                                            # (180)
                                            # approached from bottom:
                                            elif curR == prvR - 1:
                                                q.append((curR, curC, curR + directions[0][0], curC + directions[0][1],
                                                    directions[0], score + 1, startingPoint, False))

                                            # approached from left
                                            elif curC == prvC + 1:
                                                q.append((curR, curC, curR + directions[3][0], curC + directions[3][1],
                                                    directions[3], score + 1, startingPoint, False))

                                        # Triangle 2
                                        elif mat[curR][curC] == 2:
                                            # approached from top
                                            if curR == prvR + 1:
                                                q.append((curR, curC, curR + directions[1][0], curC + directions[1][1],
                                                    directions[1], score + 1, startingPoint, False))

                                            # approached from left
                                            elif curC == prvC + 1:
                                                q.append((curR, curC, curR + directions[3][0], curC + directions[3][1],
                                                    directions[3], score + 1, startingPoint, False))

                                            # (90 degree turn)
                                            # approached from bottom
                                            elif curR == prvR - 1:
                                                q.append((curR, curC, curR + directions[2][0], curC + directions[2][1],
                                                    directions[2], score + 1, startingPoint, False))

                                            # approached from right
                                            elif curC == prvC - 1:
                                                q.append((curR, curC, curR + directions[0][0], curC + directions[0][1],
                                                        directions[0], score + 1, startingPoint, False))

                                        elif mat[curR][curC] == 3:
                                            # (90 degree turn)
                                            # approached from bottom
                                            if curR == prvR - 1:
                                                q.append((curR, curC, curR + directions[3][0], curC + directions[3][1],
                                                    directions[3], score + 1, startingPoint, False))

                                            # approached from left
                                            elif curC == prvC + 1:
                                                q.append((curR, curC, curR + directions[0][0], curC + directions[0][1],
                                                    directions[0], score + 1, startingPoint, False))

                                            # (180)
                                            # approached from top
                                            elif curR == prvR + 1:
                                                q.append((curR, curC, curR + directions[1][0], curC + directions[1][1],
                                                    directions[1], score + 1, startingPoint, False))

                                            # approached from right
                                            elif curC == prvC - 1:
                                                q.append((curR, curC, curR + directions[2][0], curC + directions[2][1],
                                                    directions[2], score + 1, startingPoint, False))

                                        elif mat[curR][curC] == 4:
                                            # (90 degree turn)
                                            # approached from top
                                            if curR == prvR + 1:
                                                q.append((curR, curC, curR + directions[3][0], curC + directions[3][1],
                                                    directions[3], score + 1, startingPoint, False))

                                            # approached from left
                                            elif curC == prvC + 1:
                                                q.append((curR, curC, curR + directions[1][0], curC + directions[1][1],
                                                    directions[1], score + 1, startingPoint, False))

                                            # (180)
                                            # approached from bottom
                                            elif curR == prvR - 1:
                                                q.append((curR, curC, curR + directions[0][0], curC + directions[0][1],
                                                    directions[0], score + 1, startingPoint, False))

                                            # approached from right
                                            elif curC == prvC - 1:
                                                q.append((curR, curC, curR + directions[2][0], curC + directions[2][1],
                                                    directions[2], score + 1, startingPoint, False))

                                    # If the ball falls into a wormhole
                                    elif (curR, curC) in wormholes:
                                        if wormholePassed:
                                            q.append((curR, curC, curR + direction[0], curC + direction[1], direction, score,
                                                startingPoint, False))

                                        else:
                                            for key in wormholes.keys():
                                                if (curR, curC) == key:
                                                    continue

                                                if wormholes[(curR, curC)] == wormholes[key]:
                                                    q.append((curR, curC, key[0], key[1], direction,
                                                              score, startingPoint, True))
                                                    break

        return f"#{T} {maxScore}"

sys.stdin = open("pinball_input.txt", "r")
T = int(input())
sol = Solution()
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N = int(input().split()[0])
    mat = [list(map(int, input().split())) for _ in range(N)]
    print(sol.do(test_case, N, mat))
    # ///////////////////////////////////////////////////////////////////////////////////
