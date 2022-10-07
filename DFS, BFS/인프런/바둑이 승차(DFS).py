# 트럭의 적재용량은 C킬로그램
# 철수는 C킬로그램을 넘지 않으면서 바둑이들을 가장 무겁게 태우고 싶다
# 철수가 트럭에 태울 수 있는 가장 무거운 무게를 구해라

# 입력
# 1. 자연수 C, N
# 2. N마리 바둑이의 무게

# 출력
# 1. 가장 무거운 무게 출력

# 답은 맞지만 시간 초과
import sys
from collections import deque
def DFS(L, sum):
    if L==n:
        global result #전역변수를 함수내에서 변경하기 위해 전역변수 설정
        if sum>c: # 무게가 초과하는 경우
            return
        if result<sum:
            result=sum
    else:
        DFS(L+1, sum+weight[L]) #바둑이를 태울 경우
        DFS(L+1, sum) #바둑이를 태우지 않을 경우


c, n = map(int, input().split())
weight=[]
result=-21470000
for i in range(5):
    weight.append(int(input()))
DFS(0,0)
print(result)

# 정답
def dfs(L, sum, tsum):
    global result

    if sum+(total-tsum)<result: # 지금까지 값에 남은 바둑이를 모두 더한 값이 제일 큰 값보다 작으면 그냥 넘어감
        return
    if sum>C:
        return
    if L==N:
        if sum>result:
            result=sum
    else:
        dfs(L+1, sum+weight[L], tsum+weight[L])

        dfs(L+1, sum, tsum+weight[L]) #tsum의 경우는 바둑이를 탑승하지 않았어도 더한다.


C, N = map(int, input().split())
weight = list(map(int, input().split()))
result=-21470000
total=sum(weight)
dfs(0,0, 0)
print(result)
