# 거스름돈을 가장 적은 수의 동전으로 교환해주려면 어떻게 주면 되는가?
# 각 단위의 동전은 무한정 쓸 수 있다.

# 입력
# 1. 동전의 종류 개수 N
# 2. N개의 동전의 종류
# 3. 거슬러줄 금액 M
# 각 동전의 종류는 100원을 넘지 않음

# 출력
# 첫번째 줄에 거슬러 줄 동전의 최소 개수 출력


def dfs(L, sum):
    global cnt
    # 굳이 최소 cnt 값 이상보다 계산할 필요 없음
    if L>cnt:
        return 
    # 거스름 돈보다 값이 커지면 넘어가지
    if sum>M:
        return
    # 거스름 돈이 같아지면 최소 cnt값과 현재 Level값을 비교하여 작으면 cnt에 현재 Level값 넣기
    if sum==M:
        if L<cnt:
            cnt=L

    else:
        for i in range(N):
            dfs(L+1, sum+coin[i])

N=int(input()) # 동전의 종류 개수
coin=list(map(int, input().split())) # 동전의 종류
coin.sort(reverse=True)
M=int(input()) # 거슬러 줄 금액
cnt=2147000000
dfs(0,0)
print(cnt)
