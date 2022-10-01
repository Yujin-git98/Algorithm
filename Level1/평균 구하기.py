def solution(arr):
    num=len(arr)
    cnt=0
    for i in arr:
        cnt+=i
    answer=cnt/num
    return answer
