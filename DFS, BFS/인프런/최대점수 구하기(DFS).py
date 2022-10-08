# 최대점수 구하기(DFS)
# N개의 문제를 풀때 얻는 점수와 걸리는 시간이 주어진다.
# 제한시간 M 안에 N개의 문제 중 최대점수를 얻을 수 있도록 해야 한다.
# 해당문제는 해당 시간이 걸리면 푸는 것으로 간주하고 한 유형당 한개만 풀수 있다.

#입력
# 1. 문제의 개수N, 제한시간M
#2. N줄에 걸쳐 문제를 풀었을 떄의 점수와 푸는데 걸리는 시간

# 출력
# 제한 시간안에 얻을 수 있는 최대 점수 출력
def dfs(L, s, t):
    global res
    if t>m: # 시간이 넘어가면 가지치기
        return

    if L==n:
        if s>res: #기존의 결과보다 s가 크면 바꾸기
            res=s
    else:
        dfs(L+1, s+score[L], t+time[L]) #문제를 풀때
        dfs(L+1, s, t) # 문제를 풀지 않을때때

n, m=map(int, input().split())
time=[]
score=[]
for i in range(n):
    a, b = map(int, input().split())
    time.append(b)
    score.append(a)
res=-214700000
dfs(0,0,0)
print(res)
