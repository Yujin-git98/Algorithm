# 숫자를 str으로 변경하여 각 자릿수를 구한다.
def sum_digit(number):
    return sum([int(i) for i in str(number)])
  
# 재귀함수를 이용하여 각 자릿수를 구한다.
def sum_digit(number):
    if number < 10:
        return number;
    return (number % 10) + sum_digit(number // 10) 
