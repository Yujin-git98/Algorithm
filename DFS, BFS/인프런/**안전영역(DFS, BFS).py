# 안전영역(BFS, DFS)
# 어떤 지역의 높이 정보를 파악한다. 그 다음에 그 지역에 많은 비가 내렸을 떄
# 물에 잠기지 않는 안전한 영역이 최대로 몊개가 만들어지는지조사한다
# 문제를 간단히 하기 위해 장마철에 내리는 비의 양에 따라 일정한 높이 이하의 모든 지점은 모두 물에 잠긴다고 가정한다.
# 지역의 높이정보는 행과 열이 각각N인 2차원배열형태로 주어진다.
# 높이 4 이하인 모든 지점에 물이 잠겼다고 하면 물에 잠기는 지점을 회색으로 표현한다.
# 물에 잠기지 않은 안전한 지역은 흰색인 부분이 위, 아래, 오, 왼으로 인접하며 그 크기가 최대인 영역이다.
dx=[-1, 0, 1, 0]
dy=[0, 1, 0, -1]

def dfs(x, y, h):
    ch[x][y]=1 # 지금 잇는 위치를 체크리스트에 추가
    for i in range(4):
        xx=x+dx[i]
        yy=y+dy[i]
        if 0<=xx<n and 0<=yy<n and ch[xx][yy]==0 and map[xx][yy]>h:
            dfs(xx, yy, h)

n=int(input())
cnt=0 #안전정보 몇개
res=0 #정답 저장
map=[list(map(int, input().split())) for _ in range(n)] #map을 건들면 안됨
for h in range(100): #높이는 1부터 100까지니까
    ch=[[0]*n for _ in range(n)] # 높이가 바뀔때마다 체크리스트 초기화
    cnt=0
    for i in range(n):
        for j in range(n):
            if map[i][j]>h and ch[i][j]==0:
                cnt+=1
                dfs(i, j, h)
    res=max(res, cnt) # 최대값을 구함
    if cnt==0:
        break # 만약 9보다 큰값이 없는데 높이가 9이면 모두 0이됨.
print(res)
