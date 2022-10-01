# 나의 코드
def solution(phone_number):
    answer = ''
    
    if len(phone_number)==4:
        answer=phone_number
    phone_number=list(phone_number)
    for i in range(len(phone_number)-4):
        phone_number[i]='*'
        answer=''.join(phone_number)
    return answer

# 참고 코드
# 문자열도 곱셈이 가능함
def hide_numbers(s):
    return "*"*(len(s)-4) + s[-4:]
