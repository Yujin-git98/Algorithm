# 동전 분배하기(DFS)
# N개의 동전을 A, B, C 세명에게 나누어 주려고 한다.
# 세명이 받은 각각의 총액을 계산해 총액이 가장 큰 사람과 가장 작은 사람의 차가 최소가 되도록 해라
# 단 세 사람의 총액은 서로 달라야 한다.

# 입력
# 1. 동전의 개수 N
# 2. N줄에 걸쳐 각 동전의 금액이 주어짐

# 출력
# 총액이 가장 큰 사람과 가장 작은 사람의 차 중에서 최소를 구해라
def dfs(L):
    global res
    if L==n:
        cha=max(money)-min(money)
        if cha<res: # res가 최소가 되는 값을 찾는 과정. 단, A, B, C가 모두 다를 때만 구한다.
            tmp=set()
            for x in money:
                tmp.add(x)
            if len(tmp)==3:
                res=cha
    else:
        for i in range(3): #가지가 뻗어나가는 것은 3가지(A, B, C)
            money[i]+=coin[L] #현재 돈에서 coin[L]을 더함
            dfs(L+1)
            money[i]-=coin[L]


n=int(input())
coin=[]
for i in range(n):
    c=int(input())
    coin.append(c)
money=[0]*3
res=21470000
dfs(0)
print(res)
