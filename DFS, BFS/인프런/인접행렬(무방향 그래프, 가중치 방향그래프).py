#무방향그래프
N, M = map(int, input().split()) #N은 노드 번호, M은 간선 개수
g=[[0]*(N+1) for _ in range(N+1)]
for i in range(M): #간선정보를 입력받음
    a, b=map(int, input().split())
    g[a][b]=1 # 무방향이므로 a->b, b->a모두 고려
    g[b][a]=1

for i in range(1, N+1):
    for j in range(1, N+1):
        print(g[i][j], end=' ')
    print()

# 가중치 방향그래프
N, M = map(int, input().split()) #N은 노드 번호, M은 간선 개수
g=[[0]*(N+1) for _ in range(N+1)]
for i in range(M):
    a, b, c=map(int, input().split())
    g[a][b]=c
for i in range(1, N+1):
    for j in range(1, N+1):
        print(g[i][j], end=' ')
    print()
