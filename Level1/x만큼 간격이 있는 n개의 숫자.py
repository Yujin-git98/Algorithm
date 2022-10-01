# 나의 코드 1.
def solution(x, n):
    answer = []
    cnt=x
    
    for i in range(n):
        answer.append(cnt)
        cnt+=x

    return answer


# 나의 코드 2.
def solution(x, n):
    answer = []
    cnt=x
    
    if x>0:
        answer=[i for i in range(x, x*n+1, x)]
    elif x==0:
        answer=[0 for i in range(n)]
    else:
        answer=[i for i in range(x, x*n-1, x)]

    return answer
 
# 참고 코드 1.
def number_generator(x, n):
    # 함수를 완성하세요
    return [i * x + x for i in range(n)]
print(number_generator(2, 5))
