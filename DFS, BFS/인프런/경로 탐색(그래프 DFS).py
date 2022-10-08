# 경로 탐색(그래프 DFS)
# 방향그래프가 주어지면 1번 정점에서 N번 정점으로 가는 모든 경로의 가지 수를 출력하는 프로그램을 작성
# 한번 방문한 노드는 다시 방문하지 않도록 함

# 입력
# 정점의 수 N, 간선의 수 M
# M줄에 걸쳐 연결정보가 주어짐

# 출력
# 총 가지수를 출력

def dfs(v):
    global cnt
    if v==N:
        cnt+=1
        for x in path:
            print(x, end=' ')
        print()
    else:
        for i in range(1, N+1):
            if g[v][i]==1 and ch[i]==0:
                ch[i]=1
                path.append(i)
                dfs(i)
                path.pop()
                ch[i]=0


N, M = map(int, input().split())
g=[[0]*(N+1) for _ in range(N+1)]
ch=[0]*(N+1)
for i in range(M):
    a, b = map(int, input().split())
    g[a][b]=1 # 방향 그래프
cnt=0
path=[]
path.append(1)
ch[1]=1
dfs(1)
print(cnt)
