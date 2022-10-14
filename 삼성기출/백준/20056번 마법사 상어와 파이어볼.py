# 20056번 마법사 상어와 파이어볼
# nxn 격자. 파이어볼 M개
# 가장 처음에 파이어볼은 각자 위치에서 이동을 대기하고 있다.
# i번 파이어볼의 위치는 (ri, ci) 질량은 mi, 방향은 di 속력은 si이다.
# 격자의 행과 열은 1번부터 N번까지 번호가 매겨져 있고, 1번 행은 N번과 연결되어 있고, 1번 열은 N번열과 연결되어 있다.
# 파이어볼의 방향은 인접한 8개의 칸의 방향을 의미하며, 정수로는 0~7 : 상, 상우, 우, 우하, 하, 하좌, 좌, 좌상
# 마법사 상어가 파이어볼에게 이동 명령 하면 행동 순서
# 1. 모든 파이어볼이 자신의 방향, 속력 칸만큼 이동한다.
#   이동하는 중에는 같은 칸에 여러 개의 파이어볼이 있을 수도 있다.
# 2. 이동이 모두 끝난 뒤, 2개 이상의 파이어볼이 있는 칸에서는 다음과 같은 일이 일어난다.
#   1. 같은 칸에 있는 파이어볼은 모두 하나로 합쳐진다.
#   2. 파이어볼은 4개의 파이어볼로 나누어진다.
#   3. 나누어진 파이어볼의 질량, 속력, 방향은 다음과 같다.
#       1. 질량은 ⌊(합쳐진 파이어볼 질량의 합)/5⌋이다.
#       2. 속력은 ⌊(합쳐진 파이어볼 속력의 합)/(합쳐진 파이어볼의 개수)⌋이다.
#       3. 합쳐지는 파이어볼의 방향이 모두 홀수이거나 모두 짝수이면, 방향은 0, 2, 4, 6이 되고,
#          그렇지 않으면 1, 3, 5, 7이 된다.

# 8개 방향
dx=[-1, -1, 0, 1, 1, 1, 0, -1]
dy=[0, 1, 1, 1, 0, -1, -1, -1]

n, m, k=map(int,input().split()) # nxn 격자, 파이어볼 m개, k번 이동을 명령함
#파이어볼 m개에 대한 정보 r, c, m, s, d
fireballs=[]
for _ in range(m):
     _r, _c, _m, _s, _d = list(map(int, input().split()))
     fireballs.append([_r-1, _c-1, _m, _s, _d]) #문제는 행, 열이 1부터 시작하니까
# 서로 다른 두 파이어볼의 위치가 같은 경우는 입력으로 주어지지 않는다. 즉, 처음에는 다 하나씩 가지고 있다.

board=[[[] for _ in range(n)] for _ in range(n)]
for i in range(k):
    while fireballs:
        r, c, m, s, d=fireballs.pop(0) # 맨 첫번째부터
        nr=(r+dx[d]*s)%n
        nc=(c+dy[d]*s)%n
        board[nr][nc].append([m, s, d]) # 파이어볼이 위치한 칸에 m,s,d 정보를 넣어줌

    # 파이어볼이 2개 이상인지 체크
    for x in range(n):
        for y in range(n):
            if len(board[x][y])>1: # 2개 이상이면 4개의 파이어볼로 쪼개기
                sum_m, sum_s, cnt_odd, cnt_even, cnt = 0, 0, 0, 0, len(board[x][y])
                while board[x][y]:
                    _m, _s, _d = board[x][y].pop(0)
                    sum_m+=_m
                    sum_s+=_s
                    if _d%2==0:
                        cnt_even+=1
                    else:
                        cnt_odd+=1
                if cnt_even==cnt or cnt_odd==cnt:
                    nd=[0,2,4,6]
                else:
                    nd=[1,3,5,7]
                if sum_m//5!=0: #질량이 0이면 소멸
                    for d in nd:
                        fireballs.append([x, y, sum_m//5, sum_s//cnt, d])
            # 파이어볼이 1개인 경우
            if len(board[x][y])==1:
                fireballs.append([x, y]+board[x][y].pop())
result=0
while fireballs:
    r, c, m, s, d = fireballs.pop()
    result+=m
print(result)







