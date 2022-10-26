# 우물 안 개구리
# 헬스장에서 n명의 회원이 운동을 하고 있다. 각 회원은 1에서 n 사이의 번호가 부여되어 있고
# i번 회원이 들 수 있는 역기의 무게는 Wi이다. 회원들 사이에는 m개의 친분관계  (Aj, Bj)가 있다.
# (Aj, Bj)는  Aj번 회원과 Bj번 회원이 친분 관계가 있다는 것을 의미한다.
# i번 회원은 자신과 친분 관계가 있는 다른 회원보다 들 수 있는 역기의 무게가 무거우면 자신이 최고라고 생각한다.
# 단 누구와도 친분이 없는 멤버는 본인이 최고라고 생각한다.
# 이 헬스장에서 자신이 최고라고 생각하는 회원은 몇명인가?
n, m= map(int, input().split())
weight=list(map(int, input().split()))
ab=[]
best=[True]*n


for _ in range(m):
   a, b = map(int, input().split())
   ab.append([a-1,b-1])

for a, b in ab:
   if weight[a]>weight[b]:
      #best[a]=2
      best[b]=False
   elif weight[a]<weight[b]:
      #best[b]=2
      best[a]=False
   else:
      best[a] = False
      best[b] = False
cnt=0
for mem in best:
   if mem==True:
      cnt+=1
print(cnt)
