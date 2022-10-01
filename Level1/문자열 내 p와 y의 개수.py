# 나의 코드
def solution(s):
    answer = False
    s=s.lower()
    print(s)
    cnt_p=0
    cnt_y=0
    for i in s:
        if i=='p':
            cnt_p+=1
        elif i=='y':
            cnt_y+=1
    if cnt_p==cnt_y :
        answer=True
    if cnt_p==0 and cnt_y==0:
         answer=True
    return answer

# 참고 코드 1. 
# lower함수로 소문자를 구하고 count 함수로 p 개수를 구한다.
# 둘다 개수가 0일 경우에는 return False

def numPY(s):
    # 함수를 완성하세요
    return s.lower().count('p') == s.lower().count('y')
