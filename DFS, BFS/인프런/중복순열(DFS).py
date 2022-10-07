# 1부터 N까지 번호가 적힌 구슬이 있다.
# 중복을 허락하여 M번을 뽑아 일렬로 나열하는 방법을 출력

# 입력
# 자연수 N,M

# 출력
# 중복 순열 결과 출력, 맨 마지막 줄에 총 경우의 수 출력

def dfs(L):
    global cnt
    if L==M:
        for i in range(M):
            print(res[i], end=' ')
        print()
        cnt+=1


    else:
        for i in range(1, N+1):
            res[L]=i
            dfs(L+1)


N, M=map(int, input().split())
cnt=0
res=[0]*M
dfs(0)
print(cnt)
