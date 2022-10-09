# 미로탐색 경로의 가지수(DFS)
# 7*7 격자판 미로를 탈출하는 최단경로의 경로수 출력
# 경로수는 출발점에서 도착점까지 가는데 이동한 횟수를 의미한다.
# 출발점은 격자의 (1, 1) 좌표이고 탈출 도착점은 (7, 7) 좌표이다.
# 격자판의 1은 벽이고 0은 도로이다.
# 격자판의 움직임은 상하좌우로만 움직인다.

#입력
# 7*7 격자판의 정보가 주어진다.

#출력
# 경로의 가지수를 출력한다

dx=[-1, 0, 1, 0]
dy=[0, 1, 0, -1]
def dfs(x, y):
    global cnt
    if x==6 and y==6:
        cnt+=1
    else:
        for i in range(4):
            sx=x+dx[x]
            sy=y+dy[y]
            if 0<=sx<=6 and 0<=sy<=6 and board[sx][sy]==0:
                board[sx][sy]=1
                dfs(sx, sy)
                board[sx][sy]=0 #체크한것을 풀어줌


board = [list(map(int, input().split())) for _ in range(7)]
cnt=0
board[0][0]=1 #첫출발점
dfs(0,0)
print(cnt)


