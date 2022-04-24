
class Solution:
    def do(self, test_case, magnets, rotations):
        score = 0

        for chosen, direction in rotations:
            chosenIdx = chosen - 1
            bucket = [0] * 4
            bucket[chosenIdx] = (magnets[chosenIdx][6], magnets[chosenIdx][2])

            for i in range(4):
                if i == chosenIdx:
                    continue

                bucket[i] = (magnets[i][6], magnets[i][2])

            dirBucket = [0] * 4
            dirBucket[chosenIdx] = direction

            # Left
            prvIdx = chosenIdx
            for curIdx in range(chosenIdx - 1, -1, -1):
                cur = bucket[curIdx]; prv = bucket[prvIdx]
                if prv[0] != cur[1]:
                    dirBucket[curIdx] = -1 * dirBucket[prvIdx]
                else:
                    dirBucket[curIdx] = 0
                prvIdx = curIdx

            # Right
            prvIdx = chosenIdx
            for curIdx in range(chosenIdx + 1, 4):
                cur = bucket[curIdx]; prv = bucket[prvIdx]
                if prv[1] != cur[0]:
                    dirBucket[curIdx] = -1 * dirBucket[prvIdx]
                else:
                    dirBucket[curIdx] = 0
                prvIdx = curIdx

            # Rotate
            for i in range(4):
                if dirBucket[i] == 1:
                    tmp = magnets[i].pop()
                    magnets[i].insert(0, tmp)

                elif dirBucket[i] == -1:
                    tmp = magnets[i].pop(0)
                    magnets[i].append(tmp)

        score += magnets[0][0]
        for i in range(1, 4):
            score += (magnets[i][0] * 2) ** i

        return f"#{test_case} {score}"

sys.stdin = open("magnet_input.txt", "r")
T = int(input())
sol = Solution()
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    K = int(input().split()[0])
    magnets = [list(map(int, input().split())) for _ in range(4)]
    rotations = [list(map(int, input().split())) for _ in range(K)]
    print(sol.do(test_case, magnets, rotations))
    # ///////////////////////////////////////////////////////////////////////////////////
