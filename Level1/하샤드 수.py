def solution(x):
    answer = False
    cnt=0
    for i in str(x):
        cnt+=int(i)
    if x%cnt==0:
        answer =True
    return answer
