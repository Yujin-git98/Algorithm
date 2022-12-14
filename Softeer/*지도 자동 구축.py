# 지도 자동 구축
# 정사각형을 이루는 점 4개를 고르고 그 후에는 다음과 같은 과정을 거쳐 모양이 만들어진다
# 정사각형의 각 변의 중앙에 점을 하나 추가한다.
# 정사각형의 중심에 점을 하나 추가한다.
# 각 단계(N)가 계속해서 커져갈수록 점의 수가 커져간다.

n=int(input())
# N의 최댓값은 15이기 때문에 0단계~15단계 총 16개 칸 생성
dp=[0]*16
# start 지점의 한변의 점의 개수 = 2
dp[0]=2

# N번째 단계의 한 변의 점의 개수는 (N-1번째 점의 개수 + N-1번째 점의 개수 -1)과 같다
# 반으로 나누면서 중간에 겹치는 점이 발생하기 때문에 1을 빼준다.
for i in range(1, n+1):
    dp[i]=dp[i-1]+(dp[i-1]-1)
# print(dp) : 각 단계에서 한 변의 점의 개수
print(dp[n]**2) # 총 점의 개수 = 한 변의 점 개수의 제곱
