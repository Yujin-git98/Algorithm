# 등산경로(DFS)
# 등산 경로 지도 N*N, 각 구역에는 높이가 나타남
# 어떤 구역에서 다른 구역으로 등산할 때는 위, 아래, 왼, 오 중 더 높은 구역으로만 이동할 수있도록 설계
# 등산로의 출발지는 전체 영역에서 가장 낮은 곳이고 목적지는 가장 높은 곳이다.
# 출발지와 목적지는 유일하다.
# 출발지에서 도착지로 갈수있는 등산경로가 몇가지인가?

# 입력
# 첫번째 줄 N이 주어지고 그 다음줄에 지도정보가 주어짐

# 출력
# 등산 경로 가지수

def dfs(x, y):
    global cnt
    if x==ex and y==ey:
        cnt+=1
    else:
        for i in range(4):
            xx=x+dx[i]
            yy=y+dy[i]
            if 0<=xx<n and 0<=yy<n and board[x][y]<board[xx][yy] and ch[xx][yy]==0:
                ch[xx][yy]=1
                dfs(xx, yy)
                ch[xx][yy]=0

n=int(input())
board=[[0]*n for _ in range(n)] # 지도를 저장할 공간
ch=[[0]*n for _ in range(n)] # 체크리스트
max=-21470000   # 지도에서 최대값을 찾기 위해 초기화
min=21470000    # 지도에서 최솟값을 찾기 위해 초기화
dx=[-1, 0, 1, 0]
dy=[0, 1, 0, -1]
for i in range(n):
    tmp=list(map(int, input().split())) # 지도에서 한 행만 읽어들임
    for j in range(n):
        if tmp[j]<min:  # 한행에서 최솟값을 찾음
            min=tmp[j]
            sx=i # start x  # 최솟값을 시작 x, y로 지정
            sy=j # start y
        if tmp[j]>max:  # 한행에서 최댓값을 찾음
            max=tmp[j]
            ex=i # end x    # 최댓값을 끝 x, y로 지정
            ey=j # end y
        board[i][j]=tmp[j]  # 전체 지도를 board에 저장
ch[sx][sy]=1 # 체크리스트 초기화
cnt=0
dfs(sx, sy)
print(cnt)

