# 나의 풀이
def solution(s):
    answer = ''
    index=len(s)//2
    if len(s)%2==0:
        answer=s[index-1:index+1]
    else:
        answer=s[index]
    
    return answer
  
# 참고 풀이
def string_middle(str):
    # 함수를 완성하세요

    return str[(len(str)-1)//2:len(str)//2+1]
