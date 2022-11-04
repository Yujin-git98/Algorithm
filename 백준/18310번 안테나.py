# 18310번 안테나
# 일직선 상의 마을에 여러 채의 집이 위치함
# 특정 위치의 집에 특별히 한 개의 안테나를 설치함
# 안테나로부터 모든 집까지의 거리의 총 합이 최소가 되도록 설치하려고 함
# 안테나는 집이 위치한 곳에만 설치 가능
# 논리적으로 동일한 위치에 여러개의 집이 존재하는 것이 가능

n=int(input())
antena=list(map(int,input().split()))
# 핵심 아이디어는 중간값에 해당하는 위치의 집에 안테나를 설치했을 떄
# 안테나로부터 모든 집까지의 거리의 총합이 최소가 된다는 것이다.
# [1 2 3 5 8 9] 일때, 중간값인 3, 5일 경우 거리의 총합이 16으로 제일 작다.
# 안테나 설치할 수 있는 위치값이 여러개일 경우 가장 작은 값을 출력
antena.sort()
print(antena[(n-1)//2])


## 시간 초과
n=int(input())
result=[]
cnt=0
antena=list(map(int,input().split()))
antena.sort()
for i in antena:
    cnt=0
    for j in antena:
        cnt+=abs(i-j)
    result.append(cnt)
min_num=min(result)
for k in range(len(antena)):
    if result[k]==10:
        print(antena[k])
        break
