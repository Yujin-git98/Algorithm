# 송아지 찾기(BFS : 상대트리탐색)
# 현수의 위치와 송아지의 위치가 직선상의 좌표 점으로 주어지면 현수는 현재 위치에서 송아지 위치까지 다음과 같이 이동한다
# 한 번의 점프로 앞으로 1, 뒤로 1, 앞으로 5를 이동할 수 있다.
# 최소 몇 번의 점프로 현수가 송아지의 위치까지 갈 수 있는지 구하는 프로그램을 작성

# 입력
# 현수의 위치 S, 송아지의 위치 E

# 출력
# 점프의 최소횟수

from collections import deque
max=10000 # 좌표의 max
ch=[0]*(max+1) # 0부터 생기니까 max+1
dis=[0]*(max+1)
n, m = map(int, input().split()) #n은 현수의 위치, m은 송아지 위치
ch[n]=1
dis[n]=0
dq=deque()
dq.append(n)
while dq:
    now=dq.popleft()
    if now==m:
        break
    for next in (now-1, now+1, now+5):
        if 0<next<=max: # 좌표는 0보다 커야함
            if ch[next]==0:
                dq.append(next)
                ch[next]=1
                dis[next]=dis[now]+1
print(dis[m])
