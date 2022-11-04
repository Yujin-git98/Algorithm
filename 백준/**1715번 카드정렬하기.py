# 1715번 카드 정렬하기
# 정렬된 두 묶음의 숫자 카드
# 각 묶음의 카드 수를 A, B라 하면 보통 두 묶음을 합쳐서 하나로 만드는데 A+B번 비교해야함
# 카드를 두 묶음씩 골라 서로 합쳐나간다면 고르는 순서에 따라 비교 횟수가 매우 달라짐
# N개의 숫자 카드 묶음이 각각의 크기가 주어질 때, 최소한 몇 번의 비교가 필요한지 구해라

import heapq

n=int(input())
heap=[]
for i in range(n):
    data=int(input())
    heapq.heappush(heap, data)
result=0
# 힙에 원소가 1개 남을때까지
while len(heap)!=1:
    # 가장 작은 2개의 카드 묶음 꺼내기
    one=heapq.heappop(heap) # 힙은 가장 작은 원소부터 pop
    two=heapq.heappop(heap)
    # 카드 묶음을 합쳐서 다시 삽입
    sum_value=one+two
    result+=sum_value
    heapq.heappush(heap, sum_value)
print(result)
