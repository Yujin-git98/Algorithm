# 나의 코드
# 시행착오 : 조합 함수를 몰라서 검색했다. 암기하자
from itertools import *
def isprime(n):
    for i in range(2, int(n*0.5)+1):
        if n%i==0:
            return False
    return True

def solution(nums):
    cnt=0
    coms = list(combinations(nums, 3))
    for com in coms:
        if isprime(sum(com)):
            cnt+=1
    answer=cnt            

    return answer
