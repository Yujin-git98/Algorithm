# 자연수 N이 주어지면 1부터 N까지의 원소를 갖는 집합의 부분집합을 모두 출력

# 입력
# 자연수 N

# 출력
# 첫번째 줄부터 각 줄에 하나씩 부분집합을 출력
def dfs(L):
    if L==N+1:
        for i in range(1, N+1):
            if num[i]==1:
                print(i, end=' ')
        print()
    else:
        num[L]=1
        dfs(L+1)
        num[L]=0
        dfs(L+1)


N=int(input())
num=[0]*(N+1)
dfs(1)
