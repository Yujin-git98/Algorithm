# 사과나무(BFS)
# 현수의 농장은 N*N 격자, 각 격자 안에는 한 그루의 사과나무가 심어져 있다
# N의 크기는 항상 홀수이다. 사과 수확할 때 다이아몬드 모양의 격자판만 수확
# 수확하는 사과의 총개수를 출력해라

# 입력
# 자연수 N(홀수)
# N줄에 걸쳐 각 줄에 N개의 자연수가 주어진다. 이 자연수는 각 격자안에 있는 사과나무에 열린 사과의 개수이다.
# 각 격자안의 사과의 개수는 100을 넘지 않는다.

# 출력
# 수확한 사과의 총 개수
from collections import deque
n=int(input()) # 홀수인 격자판 길이
a=[list(map(int, input().split())) for _ in range(n)] #격자판
ch=[[0]*n for _ in range(n)]   # 체크리스트
sum=0   # 사과의 총 개수
# 위, 오른, 아래, 왼 탐색하기 위한 배열 dx, dy 생성
dx=[-1, 0, 1, 0]
dy=[0, 1, 0, -1]
dq=deque()
dq.append(a[n//2][n//2])    # 맨 가운데 값으로 초기화
ch[n//2][n//2]=1    # 체크리스트 초기화
sum+=a[n//2][n//2]  # 맨가운데 사과 개수로 초기화
L=0
while True:
    if L==n//2:
        break
    size=len(dq) #size는 1
    for i in range(size):
        tmp=dq.popleft()
        for j in range(4):
            x=tmp[0]+dx[j]
            y=tmp[0]+dy[j]
            if ch[x][y]==0:
                sum+=a[x][y]
                ch[x][y]=1
                dq.append((x, y))

