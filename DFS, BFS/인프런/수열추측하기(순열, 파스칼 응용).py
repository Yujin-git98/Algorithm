# 수열추측하기(순열, 파스칼 응용)
# 가장 윗줄에 1부터 N까지의 숫자가 한 개씩 적혀 있다.
# 둘째 줄부터 차례대로 파스칼의 삼각형처럼 위의 2개를 더한 값이 저장되게 된다.
# N과 가장 밑에 있는 숫자가 주어져 있을 때 가장 윗줄에 있는 숫자를 구하는 프로그램을 작성해라
# 답이 여러가지가 나오는 경우에는 사전순으로 가장 앞에 오는 것을 출력해야한다.

# 입력
# 1. 두개의 정수 N, F : N은 가장 윗줄에 있는 숫자의 개수, F는 가장 밑에 줄에 있는 수

# 출력
# 삼각형에서 가장 위에 들어갈 N개의 숫자를 빈 칸을 사이에 두고 출력
# 답이 존재하지 않는 경우는 입력으로 주어지지 않는다.
def dfs(L, sum):
    if L==N and sum==F: #이전에 순열 구할때 L==N 조건,
        for x in p:
            print(x, end=' ')
        print()
        exit()
    else:
        for i in range(1, N+1):
            if ch[i]==0:
                ch[i]=1
                p[L]=i
                dfs(L+1, sum+(p[L]*b[L]))
                ch[i]=0


N, F = map(int, input().split())
p=[0]*N # 순열을 저장
b=[1]*(N) # 이항계수를 저장, 이항계수의 맨왼쪽과 오른쪽은 모두 1이기 때문
ch=[0]*(N+1) # 순열만들 때 중복 제거를 위해 check
for i in range(1, N): # 이항계수 초기화
    b[i]=b[i-1]*(N-i)//i
dfs(0, 0)



# 수열 추측하기 - 라이브러리 이용
from itertools import permutations

N, F = map(int, input().split())
b=[1]*N
cnt=0
for i in range(1, N+1):
    b[i]=b[i-1]*(N-i)//i
a=list(range(1, N+1))
for tmp in permutations(a):
    sum=0
    for L, x in enumerate(tmp): #tmp 튜플 자료 중 1개씩접근 1, 2, 3, 4
        sum+=(x*b[L])
    if sum==F:
        for x in tmp:
            print(x, end=' ')
        break # 순열을 브레이크
print(cnt)
