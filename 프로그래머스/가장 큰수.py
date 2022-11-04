from itertools import permutations
"""def solution(numbers):
    res=[]
    for per in permutations(numbers, len(numbers)):
        a=''.join(str(i) for i in per) # 문자열
        res.append(a)
    res.sort(reverse=True)
    answer=res[0]
    return answer"""
def solution(numbers):
    # 주어진 배열을 문자열로 변환
    numbers=list(map(str, numbers))
    numbers.sort(key=lambda x:x*3, reverse=True)
    answer=str(int(''.join(numbers)))
    
    
    return answer
