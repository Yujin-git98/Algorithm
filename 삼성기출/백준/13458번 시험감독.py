# 총 N개의 시험장, i번 시험장에 있는 응시자의 수는 Ai명
# 총 감독관 : 한 시험장에서 감시할 수 있는 응시자 수는 B명
# 부감독관 : 한 시험장에서 감시할 수 있는 응시자 수는 C명
# 각각 시험장에 총감독관은 오직 1명만 있어야 하고 부감독관은 여러명 있어도 된다.
# 각 시험장마다 응시생들을 모두 감시해야 하낟.
# 이때 필요한 감독관 수의 최솟값을 구해라

#입력
# 1. 시험장 개수 N
# 2. 각 시험장에 있는 응시자의 수 Ai
# 3. B와 C

N=int(input())
people=list(map(int, input().split()))
B, C =map(int, input().split())
cnt=0

for i in people:
    if i>=B:
        cnt += 1
        i=i-B
        if i%C==0:
            cnt+=(i//C)
        else:
            cnt += (i // C)
            cnt+=1
    else:
        cnt+=1
print(cnt)

