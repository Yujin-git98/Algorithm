# N개의 원소로 구성된 자연수 집합
# 이 집합을 두 개의 부분집합으로 나누었을 때 두 부분집합의 원소의 합이 서로 같은 경우가 존재하면 YES 출력
# 그렇지 않으면 NO 출력
# 둘로 나뉘는 두 부분집합은 서로서 집합. 두 부분집합을 합하면 원래의 집합이 되야함

# 입력
# 1. 자연수 N
# 2. 집합의 원소 N, 각 원소는 중복되지 않는다.

# 출력
# YES 또는 NO를 출력

def dfs(L, sum):
    if L==N:
        if sum==(total-sum):
            print('YES')
            exit()

    else:
        dfs(L+1,sum+num[L])
        dfs(L+1, sum)
N=int(input())
num = list(map(int, input().split()))
total=sum(num)
dfs(0, 0)
print('NO')
