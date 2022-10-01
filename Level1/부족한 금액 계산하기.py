def solution(price, money, count):
    answer = -1
    cnt=0
    for i in range(1, count+1):
        cnt+=price*i
    if money>cnt:
        answer=0
    else:
        answer=cnt-money
    return answer
