# 동전 바꿔주기(DFS)
# k가지 동전이 각각 n1, n2, nk개씩 들어있다.
# 가게 주인은 명보에게 T원의 지폐를 동전으로 바꿔주려고 한다.
# 동전 교환방법은 여러가지가 있을 수 있다,
# 입력으로 지폐의 금액 T, 동전의 가지수 k, 각 동전 하나의 금액 pi, 개수ni
# 지폐를 동전으로 교환하는 방법의 가지수를 계산

# 입력
# 1. 지폐의 금액 T
# 2. 동전의 가지수k
# 3. 각 줄의 동전의 금액 pi, 개수 ni

# 출력
# 동전 교환 방법의 가지수를 출력

def dfs(L, sum):
    global cnt
    if sum>t: #구하고자 하는 금액보다 커지면 가지치기
        return
    if L==k:   # 5원,10원, 1원거치고 나서 sum이 20인 경우만 cnt 경우의 수에 추가
        if sum==t:
            cnt+=1

    else:
        for i in range(num[L]+1): # 5원이 0개인 경우, 1개인 경우, 2개인 경우, 3개인 경우를 구함
            dfs(L+1, sum+coin[L]*i)


t=int(input())
k=int(input())
num=[]
coin=[]
for i in range(k):
    c, n = map(int, input().split())
    coin.append(c)
    num.append(n)
cnt=0
dfs(0, 0)
print(cnt)
