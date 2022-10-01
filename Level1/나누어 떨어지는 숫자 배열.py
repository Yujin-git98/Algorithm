def solution(arr, divisor):
    answer = []
    cnt=0
    for i in arr:
        if i%divisor==0:
            answer.append(i)
    answer.sort()
    if len(answer)==0:
        answer=[-1]
    
    return answer
