# 사다리 타기(DFS)
# 사다리 표현은 2차원 격자이고 평면은 0, 사다리는 1로 표현한다.
# 특정 도착지점으로 도착하기 위해 몇번째 열에서 출발해야하는지 알고 싶다.
# 특정 도착지점은 2로 표기된다.
from collections import deque
dx=[-1, 0, 1, 0]
dy=[0, 1, 0, -1]

def dfs(x, y):
    ch[x][y]=1
    if x==0:
        print(y)
    else:
        if y-1>=0 and map[x][y-1]==1 and ch[x][y-1]==0: # 왼쪽
            dfs(x, y-1)
        elif y+1<10 and map[x][y+1]==1 and ch[x][y+1]==0: # 오른쪽
            dfs(x, y+1)
        else:
            dfs(x-1, y) #위

map=[list(map(int, input().split())) for _ in range(10)] #x가 행 y가 열
ch=[[0]*10 for _ in range(10)]
for y in range(10):
    if map[9][y]==2: # 모든 경우의 수를 다 탐색하기 어려우니까 맨 마지막행에서 최종 도착지를 찾아서 거기서 dfs한다.
        dfs(9, y)
