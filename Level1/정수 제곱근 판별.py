# 나의 코드
# for문으로 1부터 n까지 제곱한 결과 중 n과 같을 때 제곱근을 구함
# 숫자가 커지면 비효율적임
def solution(n):
    answer=0
    for i in range(1, n+1):
        if (i**2)==n:
            answer=(i+1)**2
            break
        else: 
            answer=-1
    return answer

# 참고 코드 1.
# n의 1/2 제곱을 이용하여 제곱근을 구함
def solution(n):
    answer=0
    sqrt=n**(1/2)
    if sqrt%1==0:
        answer=(sqrt+1)**2
    else:
        answer=-1
    return answer
  
# 참고 코드 2. 
# from math import sqrt를 이용하여 제곱근을 구함
# 0은 False, 1은 True를 이용하여 return
def nextSqure(n):
    from math import sqrt
    return "no" if sqrt(n) % 1 else (sqrt(n)+1)**2
