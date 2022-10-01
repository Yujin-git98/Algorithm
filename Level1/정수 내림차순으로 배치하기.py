
# 내 코드
def solution(n):
    answer=list(int(i) for i in str(n))
    answer.sort(reverse=True)
    answer =''.join(str(s) for s in answer)
    return int(answer)

# 참고 코드 1. for문 필요없이 str로 바꿔줌
def solution(n):
    ls = list(str(n))
    ls.sort(reverse = True)
    return int("".join(ls))
