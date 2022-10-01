#나의 코드 : 참조 코드 1과 아이디어는 같지만 짧게 구현하는 연습하자
def solution(n):
    string=str(n)
    cnt=0
    for i in string:
        cnt+=int(i)
    answer = cnt
    return answer

# 참조 코드 1. 숫자를 str으로 변경하여 각 자릿수를 구한다.
def sum_digit(number):
    return sum([int(i) for i in str(number)])
  
# 참조 코드 2. 재귀함수를 이용하여 각 자릿수를 구한다.
def sum_digit(number):
    if number < 10:
        return number;
    return (number % 10) + sum_digit(number // 10) 
