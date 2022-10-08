# 휴가(삼성 SW역략평가 기출문제 : DFS활용)
# 현수는 N+1일에 휴가 가기위해 남은 N일 동안 최대한 많은 상담하려고 한다.
# 상담 걸리는 일수 T, 상담했을 때 받을 수 있는 금액 P
# 얻을 수 있는 최대 수익을 구해라

# 입력
# 1. N이 주어짐
# 2. 1~N까지 순서대로 T,P 주어짐

# 출력
# 최대이익 출력

def dfs(L, sum):
    global res
    if L==n+1: # 1일부터 8일까지 
        if res<sum:
            res=sum
    else:
        if L+time[L]<=n+1:
            dfs(L+time[L], sum+pay[L])
        dfs(L+1, sum)


n=int(input())
time=[]
pay=[]
for i in range(n):
    t, p = map(int, input().split())
    time.append(t)
    pay.append(p)
time.insert(0,0) #dummy 인덱스를 1부터 시작하여 날짜를 이용하기 위해
pay.insert(0,0) #dummy
res=-1000000
dfs(1, 0)
print(res)
