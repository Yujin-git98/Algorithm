# 섬나라 아일랜드 (BFS활용)
# 섬나라 아일랜드의 지도가 주어짐
# 각 섬은 1로 표시되어 상하좌우와 대각선으로 연결되어 잇으며 0은 바다이다 ***상하좌우 대각선
# 섬나라 아일랜드에 몇개의 섬이 있는지 구하시오

#입력
# 자연수 n , 격자판 정보

#출력
# 섬의개수
from collections import deque
dx=[-1, -1, 0, 1, 1, 1, 0, -1] #시계방향으로 탐색
dy=[0, 1, 1, 1, 0, -1, -1, -1]
n=int(input())
board=[list(map(int, input().split())) for _ in range(n)]
cnt=0
res=[]
dq=deque()
for i in range(n):
    for j in range(n):
        if board[i][j]==1:
            board[i][j]=0 # 체크(지나왔다는 증거)
            dq.append((i, j))
            while dq:
                tmp=dq.popleft()
                for k in range(8):
                    xx=tmp[0]+dx[k]
                    yy=tmp[1]+dy[k]
                    if 0<=xx<n and 0<=yy<n and board[xx][yy]==1:
                        board[xx][yy]=0
                        dq.append((xx, yy))

            cnt+=1
print(cnt)
