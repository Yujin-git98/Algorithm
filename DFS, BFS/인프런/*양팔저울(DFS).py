# 양팔저울(DFS)
# 무게가 서로 다른 K개의 추와 빈그릇이 있다
# 모든 추의 무게는 정수, 그릇의 무게는 0
# 양팔저울을 한 번만 사용하여 원하는 물의 무게를 그릇에 담고자 한다.
# 주어진 모든 추 무게의 합 : S

# 입력
# 1. 자연수 K
# 2. K개의 각 추의 무게가 공백을 사이에 두고 주어짐

# 출력
# 첫번째 측정이 불가능한 가지수를 출력
def dfs(L, sum):
    global res
    if L==k:
        if 0<sum<=s:
            res.add(sum)
    else:
        dfs(L+1, sum+weight[L]) # 추와 물을 따로 올렸을 때
        dfs(L+1, sum-weight[L]) # 추와 물을 같이 올렸을 때
        dfs(L+1, sum) # 추를 올리지 않았을 때

k = int(input())
weight=list(map(int,input().split())) # 가지고 있는 추의 무게를 list로 전달
s=sum(weight) #1부터 S사이의 무게에서 측정가능한 물의 무게와 아닌 무게를 구해야함
res=set() # 결과 중에 중복 된것이 있기 때문에 중복 제거용 set 사용
dfs(0,0)
print(s-len(res)) # len(res)는 측정가능한 물의 무게 개수이고 이와 S의 차를 구하면 측정불가능한 물의 무게 개수임.
