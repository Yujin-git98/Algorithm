T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n=int(input()) # 
    board=[[0]*n for _ in range(n)]
    # 달팽이는 시계방향 : 동, 남, 서, 북
    dr=[0, 1, 0, -1] #row
    dc=[1, 0, -1, 0] #column
    x=y=0
    direction=0
    for i in range(1, n*n+1): 
        # 해당 좌표에 1부터 n까지 수를 부여한다.
        board[x][y]=i 
        # 다음 좌표를 구한다
        x+=dr[direction]  
        y+=dc[direction]
        
        # 다음 좌표의 값이 board 범위 안에 없거나, 이미 값이 부여된 경우
        if x<0 or y<0 or x>=n or y>=n or board[x][y]!=0:
            # 다음 좌표를 이전으로 돌리고
            x-=dr[direction]
            y-=dc[direction]
            # 방향을 다음 방향으로 바꾼 다음 다음 좌표를 구한다.
            direction=(direction+1)%4
            x+=dr[direction]
            y+=dc[direction]
            
    print('#%d'% test_case)
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=' ')
        print()
