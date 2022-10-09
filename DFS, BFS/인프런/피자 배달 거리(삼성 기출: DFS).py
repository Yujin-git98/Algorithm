# 피자 배달 거리(삼성 SW역량평가 기출문제 : DFS활용)
# NxN크기의 지도가 있음. 지도는 1x1크기의 격자칸으로 이루어져 있음
# 각 격자칸에는 0은 빈칸, 1은 집, 2는 피자집으로 표현됨
# 각 집마다 '피자배달거리'가 있다. 이는 해당 집과 도시에 존재하는 피자집과의 거리 중 최소값을 의미한다.
# 집과 피자집의 피자배달거리는 (x1-x2)+(y1-y2) 이다. 이떄 괄호는 절댓값으로 인식
# 피자집 M개를 선택하는 기준으로 도시의 피자 배달거리가 최소가 되는 M개의 피자집을 선택

#입력
# N, M 주어짐, 둘째줄에 도시정보 입력

# 출력
# 도시의 최소 피자배달거리

from collections import deque
dx=[-1, 0, 1, 0]
dy=[0, 1, 0, -1]

def dfs(L, s): # 조합을 구하기 위함
    global res
    if L==m:
        sum = 0  #도시의 피자거리
        for j in range(len(home)): #집의 위치
            x1=home[j][0]
            y1=home[j][1]
            dis=21470000
            for x in cb: # 피자집의 위치
                x2=shop[x][0]
                y2=shop[x][1]
                dis=min(dis, abs(x1-x2)+abs(y1-y2)) # 집과 피자집의 거리 최솟값 저장
            sum+=dis
        if sum<res:
            res=sum
    else:
        for i in range(s, len(shop)): #조합은 s부터 시작
            cb[L]=i
            dfs(L+1, i+1)
home=[]
shop=[]
n, m=map(int, input().split())
cb=[0]*m # 조합의 경우의 수를 저장
res=21470000
board=[list(map(int, input().split()))for _ in range(n)]
for i in range(n):
    for j in range(n):
        if board[i][j]==1:
            home.append((i, j))
        elif board[i][j]==2:
            shop.append((i, j))
dfs(0,0)
print(res)
