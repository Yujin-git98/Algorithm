# 강의실 배정
# 김교수는 강의실 1개에 최대한 많은 강의를 배정하려고 한다.
# 배정된 강의는 서로 겹치지 않아야 하며 수업시간의 길이와 상관없이 최대한 강의를 많이 배정하라
# 단, 두 강의의 시작 시간과 종료 시간은 겹쳐도 된다.


## 풀이 참고 코드
import sys
import heapq
n = int(sys.stdin.readline())
lec=[]
for _ in  range(n):
    s, e = list(map(int, sys.stdin.readline().split()))
    # 끝나는 시간이 가장 작은 것을 맨앞에 넣어준다.
    # 만약 시작 시간이 같을 때에는 가장 작은 시간부터 오름차순으로
    heapq.heappush(lec, (e, s))

cur=0
cnt=0
# heap 리스트가 0이 될때까지 반복한다.
while lec:
    e, s = heapq.heappop(lec)

    # 시작시간이 초기값(종료시간)보다 크거나 같으면 카운터 해준다
    # 다음 기준값은 종료시간으로 초기화해준다.
    if cur<=s:
        cnt+=1
        cur=e
print(cnt)


## 시간초과로 실패
import sys
n = int(sys.stdin.readline()) #강의 개수
lec=[]
for i in range(n):
    s, e = map(int, sys.stdin.readline().split()) # 강의 시작시간과 종료시간
    lec.append([s,e]) #저장
# 그리디 알고리즘 : 가장 빨리 끝나는 것 우선으로 하기
lec.sort(key=lambda x : (x[1], x[0]))
cur=0 # 현재 종료시간
cnt=0 # 강의 수


for i in range(n):
    s1, e1 = lec.pop(0)

    # 시작 시간이 초기값(종료 시간)보다 크거나 같으면 카운터해준다.
    if cur<=s1:
        cur=e1
        cnt+=1
print(cnt)
