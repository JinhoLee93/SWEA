class Solution:
    def do(self, N, K, num):
        # N numbers of input num, K th largest number, num
        numOfFaces = N // 4
        numArr = [char for char in num]
        res = []
 
        for i in range(numOfFaces):
            tmp = ""
            for j in range(len(numArr)):
                tmp += numArr[j]
 
                if len(tmp) == numOfFaces:
                    if tmp not in res:
                        res.append(tmp)
                    tmp = ""
 
            rotatedInt = numArr.pop()
            numArr.insert(0, rotatedInt)
 
        res = sorted(res, reverse=True)
 
        return int(res[K - 1], 16)
 
T = int(input())
sol = Solution()
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N, K = map(int, input().split())
    num = input()
    print(sol.do(N, K, num))
    # ///////////////////////////////////////////////////////////////////////////////////
