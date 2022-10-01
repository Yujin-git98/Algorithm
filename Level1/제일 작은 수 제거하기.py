# 나의 코드
# 시행착오 1. 원래 sort한 다음 pop을 하려고 했는데 그러면 원래 배열이 변경되서 안됨
def solution(arr):
    answer = []
    arr.remove(min(arr))
    if len(arr)<1:
        answer=[-1]
    else:
        answer=arr
        
    return answer
