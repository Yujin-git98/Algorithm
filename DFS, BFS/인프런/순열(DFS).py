# 1부터 N까지 번호가 적힌 구슬이 있다.
# 이 중 M개를 뽑아 일렬로 나열하는 방법을 모두 출력

# 입력
# 자연수 N, M

# 출력
# 순열의 결과 출력, 맨 마지막에는 총 경우의 수 출력
# 출력 순서는 사전순으로 오름차순으로 출력

def dfs(L):
    global cnt
    if L==M:
        for i in range(M):
            print(res[i], end=' ')
        print()
        cnt+=1
    else:
        for i in range(1, N+1):
            if ch[i]==0: # 이전에 사용한 숫자인지
                ch[i]=1
                res[L] = i
                dfs(L+1)
                ch[i]=0 # 체크해둔 것을 풀어줌

N, M =map(int, input().split())

res = [0]*N
ch = [0]*(N+1)
cnt=0
dfs(0)
print(cnt)
