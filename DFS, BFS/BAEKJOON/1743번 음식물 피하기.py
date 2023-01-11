# 1743번 음식물 피하기
# 제일 큰 음식물의 크기를 구해서 "10ra"를 외치지 않게 도와주자
# 입력으로 첫째 줄에 통로의 세로길이 N, 가로길이 M, 음식물 쓰레기 개수 K
# 다음 K개의 줄에 음식물이 떨어진 좌표 (r, c)가 주어진다.
# 이 때, r은 위에서부터, c는 왼쪽에서부터가 기준이다.


from collections import deque



dx=[-1, 1, 0, 0]
dy=[0, 0, -1, 1]

def bfs(i, j, graph, visited):
    dq = deque()
    dq.append([i, j])
    visited[i][j]=1 # 방문했음을 표시
    result=1
    while dq:
        x,y=dq.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if graph[nx][ny]==1 and visited[nx][ny]==0:
                    result+=1
                    visited[nx][ny]=1
                    dq.append([nx,ny])
    return result


n, m, k = map(int, input().split())
graph = [[0]*m for _ in range(n)]
for _ in range(k):
    a, b = map(int, input().split())
    graph[a-1][b-1]=1 # graph에서 음식물 쓰레기 있는 곳은 1, 없는 곳은 0
visited = [[0]*m for _ in range(n)] # 음식물 쓰레기가 이미 방문한 곳이면 1, 방문하지 않았으면 0
answer=0

# 그래프 문제(DFS, BFS)에서 가장 큰 덩어리를 찾는다면
# 전체 맵을 이중 for문을 통해 돌면서
# 조건을 만족하는 부분에서 bfs를 실행한다.
# 여기서 조건이란, 현재 문제에서는 음식물 쓰레기가 있는 곳의 가장 큰 덩어리를 구하라고 했으니까
# 음식물 쓰레기가 있고 방문하지 않은 곳이 조건이 된다.
# bfs의 역할은 얼마나 연결되었는지를 알려준다.
# 즉 bfs의 결과 중에서 가장 큰 값이 우리가 구하려고 하는 가장 큰 음식물의 크기가 된다
for i in range(n):
    for j in range(m):
        if graph[i][j]==1 and visited[i][j]==0: # 음식물 쓰레기가 있고, 방문하지 않은 곳
            ans=bfs(i, j, graph, visited)
            answer = max(ans,answer)

print(answer)
