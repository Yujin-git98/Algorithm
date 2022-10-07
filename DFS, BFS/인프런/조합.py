# 1부터 N까지 번호가 적힌 구슬이 있다. 이 중 M개를 뽑는 방법의 수를 출력하는 프로그램

# 입력
# 1. 자연수 N, M

# 출력
# 1. 조합의 결과 출력, 맨 마지막에 총 경우의 수 출력

# L은 level, S는 조합에서 한번 사용한 것을 제외하기 위한 Start 위치
def dfs(L, S):
    global cnt
    # 순열 방식과 동일
    if L==M:
        for i in range(M):
            print(res[i], end=' ')
        print()
        cnt += 1

    else:
        # S부터 N+1까지만 접근 -> 조합은 한 번 사용한것 다시 안쓰니까
        for i in range(S, N+1):
            res[L]=i
            dfs(L+1, i+1)


N, M =map(int, input().split())
res=[0]*(N+1)
cnt=0
dfs(0, 1)
print(cnt)
