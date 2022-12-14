from collections import deque

# 길이가 N인 컨베이어 벨트, 길이가 2N인 벨트가 컨베이어 벨트를 감싸며 돌고 있다.
# 벨트는 길이 1 간격으로 2N개의 칸으로 나뉘어져 있다.
# 벨트가 한 칸 회전하면 1번부터 2N-1번까지의 칸은 다음 번호의 칸이 있는 위치로 이동, 2N번 칸은 1번 칸으로 이동
# i번 칸의 내구도는 Ai
# 컨베이어 벨트에 로봇을 올리려고 한다.
# 1번 칸 : 올리는 위치, N번 칸 : 내리는 위치
# 로봇은 올리는 위치에만 올릴 수 있으며, 내리는 위치에 도달하면 내린다.
# 로봇은 컨베이어 벨트 위에서 스스로 이동할 수 있다.
# 로봇을 올리는 위치에 올리거나, 로봇이 어떤 칸으로 이동하면 그 칸의 내구도는 1을 빼준다
# 1. 벨트가 각 칸 위에 있는 로봇과 함께 한 칸 회전한다.
# 2. 가장 먼저 벨트에 올라간 로봇부터 벨트가 회전하는 방향으로 한칸 이동한다.
# 이때 이동하려는 곳에 로봇이 없으며, 내구도가 1 이상 남아 있어야 한다.
# 3. 올리는 위치에 있는 칸의 내구도가 0이 아니면 올리는 위치에 로봇을 올린다.
# 4. 내구도가 0인 칸의 개수가 K개 이상이라면 과정을 종료한다. 그렇지 않다면 1로 돌아간다.
# 종료되었을 때 몇번째 단계가 진행 중이었는지 구해보자

N,K=map(int, input().split())
belts=deque(map(int, input().split())) #내구도 A1, A2, ... A2N
robot=deque([0]*N)
result=0

while True:
    result+=1
    # 1. 벨트를 회전
    belts.rotate(1)
    robot.rotate(1)
    robot[N-1]=0 #N-1에 있는 로봇을 내린다.

    #2. 로봇 이동 : 이동하려는 칸에 로봇이 없고 내구도가 1 이상이여야 한다.
    for i in range(N-2, 0, -1): #N-2부터 0까지 탐색하여 가장 먼저 올라간 로봇을 찾음
        if belts[i+1]>=1 and robot[i+1]==0 and robot[i]==1:
            robot[i+1]=1 #로봇을 한 칸 전진
            robot[i]=0
            belts[i+1]-=1 # 내구도 감소
    robot[N-1]=0 # N-1에 있는 로봇을 내린다

    #3. 올리는 위치에 내구도 0아니면 로봇 올리기 & 내구도 감소
    if belts[0]!=0 and robot[0]!=1:
        robot[0]=1 # 0번째 인덱스에 로봇을 올리며 내구도를 감소한다.
        belts[0]-=1
    if belts.count(0)>=K: #내구도가 0인 위치를 구하여 K이상일 때 종료시킨다.
        break
print(result)


