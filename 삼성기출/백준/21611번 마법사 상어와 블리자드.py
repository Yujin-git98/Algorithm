n, m=map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
blizard=[list(map(int, input().split())) for _ in range(m)]

shark=[n//2, n//2]
result=[0, 0, 0]

def destroy(d, s):
    global board, n, shark
    dr=[-1, 1, 0, 0]
    dc=[0, 0, -1, 1]
    d=d-1 #방향의 배열은 0부터 시작하니까
    for i in range(1, s+1):
        r=shark[0]+dr[d]*i
        c=shark[1]+dc[d]*i

        if r<0 or c<0 or r>=n or c>=n:
            break
        #파괴
        board[r][c]=0
        a=board

def board2list():
    global board
    arr=[0]
    r = n // 2
    c = n // 2
    dr=[0, 1, 0, -1]
    dc=[-1, 0, 1, 0]
    dist=1
    move_count=0
    direction=0
    is_over=False
    while not is_over:
        move_count+=1
        for _ in range(dist):
            nr = r + dr[direction]
            nc = c + dc[direction]

            if (nr, nc) == (0, -1):
                is_over=True
                break
                # 번호 증가 및 기록
            arr.append(board[nr][nc])

            #(r, c)를 갱신
            r=nr
            c=nc

        if move_count==2: #어떠한 방향으로든 2번 이동한 경우
            dist+=1 # 이동거리 1 증가
            move_count=0 #초기화
        direction=(direction+1)%4 #방향 변경
    return arr

def move(arr): #구슬 배열에서 빈칸제거
    return [arr[i] for i in range(len(arr)) if arr[i]!=0]

# 폭발
def explore(arr):
    global result

    #구슬이 존재하지 않는 경우
    if not arr:
        return [], False

    #연속하는 구슬이 4개 이상이면 폭발
    cur_marble=arr[0]
    cur_num=1
    is_removed=False

    for i in range(1, len(arr)):
        # 같은 색의 구슬이라면
        if arr[i]==cur_marble:
            cur_num+=1
        else:
            #다른색의 구슬인데 4개 미만인경우
            if cur_num<4:
                cur_num=1
                cur_marble=arr[i]
            #다른색의 구슬인데 4개 이상인경우
            else:
                # 개수만큼 이전 구슬들 폭발
                for j in range(1, cur_num+1):
                    arr[i-j]=0
                # result에 폭발 개수 저장
                result[cur_marble-1]+=cur_num #-1을 해주는 이유는 result의 0, 1, 2는 curmable의 1, 2, 3이기 때문
                is_removed=True
                # 새로운 색으로 update
                cur_num=1
                cur_marble=arr[i]

    # 마지막으로 현재 구슬들 체크
    if cur_num >= 4:
        is_removed = True
        for j in range(1, cur_num + 1):
            arr[len(arr) - j] = 0
        result[cur_marble - 1] += cur_num

    return arr, is_removed

def make_group(arr):
    # 구슬이 존재하지 않는 경우
    if not arr:
        return []
    #그룹으로 묶어서 [구슬 개수, 구슬 번호]로 변경
    new_arr=[]
    cur_type=arr[0]
    cur_num=1

    for i in range(1, len(arr)):
        if arr[i]==cur_type:
            cur_num+=1
        else:
            # 다른 색의 구슬인 경우 그룹 [구슬 개수, 구슬 번호] 추가
            new_arr.append(cur_num)
            new_arr.append(cur_type)
            cur_num=1
            cur_type=arr[i]
    #마지막 그룹체크
    new_arr.append(cur_num)
    new_arr.append(cur_type)

    return new_arr

def list2board(arr):
    global n, shark

    # list를 회오리 모양 보드로 변경
    new_board=[[0]*n for _ in range(n)]

    # 구슬이 없다면
    if not arr:
        return new_board
    r=shark[0]
    c=shark[1]

    dr=[0, 1, 0, -1]
    dc=[-1, 0, 1, 0]
    dist=1
    move_count=0
    direction=0
    cur_arr=0
    is_over=False
    while not is_over:
        move_count+=1
        for _ in range(dist):
            nr = r + dr[direction]
            nc = c + dc[direction]

            if (nr, nc) == (0, -1):
                is_over=True
                break
                # 번호 증가 및 기록
            new_board[nr][nc]=arr[cur_arr]
            cur_arr+=1

            # 구슬이 더이상 없다면
            if cur_arr>=len(arr):
                is_over=True
                break


            #(r, c)를 갱신
            r=nr
            c=nc

        if move_count==2: #어떠한 방향으로든 2번 이동한 경우
            dist+=1 # 이동거리 1 증가
            move_count=0 #초기화
        direction=(direction+1)%4 #방향 변경
        a=new_board
    return new_board




def solution():
    global m, blizard, board, result

    for i in range(m):
        a=blizard[i][0]
        b=blizard[i][1]
        destroy(blizard[i][0], blizard[i][1]) # 방향, 거리
        arr = board2list() # 2차원 배열을 1차원으로 변경
        arr = move(arr) # 0을 제거
        while arr:
            arr, is_removed = explore(arr) # 폭발
            if not is_removed: # 더이상 폭발할 것이 없다면
                break
            arr=move(arr) #
        board=list2board(make_group(arr)) # 1차원을 2차원 배열으로 변경
    print(result[0]+2*result[1]+3*result[2])
solution()
