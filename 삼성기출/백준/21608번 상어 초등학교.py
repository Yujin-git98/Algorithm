# 21608번 상어 초등학교
# 교실 nxn 격자. 학생수는 n^2
# 학생은 1부터 n^2까지 번호가 매겨짐 ***1부터 시작 주의
# 상하좌우 인접
# 학생의 순서와 각 학생이 좋아하는 학생 4명이 조사
# 아래와 같은 규칙으로 정해진 순서대로 학생의 자리를 정한다.
#1. 비어있는 칸 중에서 좋아하는 학생이 인접한 칸에 가장 많은 칸으로 자리를 정한다.
#2. 1을 만족하는 칸이 여러 개이면, 인접한 칸 중에서 비어있는 칸이 가장 많은 칸으로 자리를 정한다.
#3. 2를 만족하는 칸도 여러 개이면 행의 번호가 작고 -> 열의 번호가 작은 칸으로 자리를 정한다.
# 자리배치가 모두 끝난 후에 만족도 조사를 한다. 학생의 만족도는 그 학생과 인접한 칸에 앉은 좋아하는 학생 주이다.
# 그 값이 0이면 만족도는 0, 1이면 1, 2이면 10, 3이면 100, 4이면 1000이다.
# 학생의 만족도의 총 합을 구해보자
import numpy
dx=[-1, 1, 0, 0]
dy=[0, 0, -1, 1]

n=int(input())
arr=[[0]*n for _ in range(n)]
students=[list(map(int, input().split())) for _ in range(n**2)]

for s in range(n**2): #학생 수만큼 for문을 돌며 자리에 앉혀줌
    student=students[s] # 학생의 정보인 번호, 선호하는 친구를 가져온다.
    tmp=[] #여기에 가능한 자리를 다 담아서 정렬 후 앉힘
    for i in range(n):
        for j in range(n):
            if arr[i][j]==0:
                like=0
                blank=0
                for k in range(4):
                    nx=i+dx[k]
                    ny=j+dy[k]
                    if 0<=nx<n and 0<=ny<n:
                        if arr[nx][ny] in student[1:]:
                            like+=1
                        if arr[nx][ny]==0:
                            blank+=1
                tmp.append([like, blank, i, j])
    tmp.sort(key=lambda x:(x[0], x[1], -x[2], -x[3]))
    l, b, i, j = tmp.pop()
    arr[i][j]=student[0]

result=0
students.sort() #여기서 정렬
for x in range(n):
    for y in range(n):
        cnt=0
        for k in range(4):
            nx=x+dx[k]
            ny=y+dy[k]
            if 0<=nx<n and 0<=ny<n:
                if arr[nx][ny] in students[arr[x][y]-1]: #현재 위치의 학생 번호 -1에 해당하는 학생정보 안에
                    #어처피 맨처음은자기자신
                    cnt+=1
                    #print(arr[nx][ny])
                    #print(students[arr[x][y]-1])
        if cnt!=0:
            result += 10 ** (cnt - 1)
print(result)


