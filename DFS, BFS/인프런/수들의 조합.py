# 수들의 조합
# N개의 정수가 주어지면 그 숫자들 중 K개를 뽑는 조합의 합이 임의의 정수 M의 배수인 개수는 몇 개가 있는지 출력

# 입력
# 1. 정수의 개수 N, 임의의 정수 K
# 2. N개의 정수
# 3. M

# 출력
# 총 가지 수
def dfs(L, S, sum):
    global cnt
    global arr
    if L==K:
        if sum%M==0:
            cnt+=1
    else:
        for i in range(S, N): # num배열의 값을 가져와야 하기 때문에 0번부터 N-1까지만 돈다.
            dfs(L+1, i+1, sum+num[i])

N, K = map(int, input().split())
num = list(map(int, input().split()))
M = int(input())
res=[0]*N
cnt=0
dfs(0,0, 0) # num배열의 값을 가져와야하기 때문에 1이 아니라 0부터 시작
print(cnt)


# 라이브러리 사용
from itertools import permutations
from itertools import combinations

N, K =map(int, input().split())
num=list(map(int, input().split()))
M = int(input())
cnt=0
res=0
for com in combinations(num, K):
    if sum(com)%M==0:
        cnt+=1
print(cnt)

