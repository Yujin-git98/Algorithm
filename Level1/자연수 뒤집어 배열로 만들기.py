# 나의 풀이
def solution(n):
    answer = []
    for i in str(n):
        answer.append(int(i))
    answer.reverse()
    return answer
  
# 참고 풀이 1. 아이디어는 같지만 간단한 풀이
def digit_reverse(n):
    return list(map(int, reversed(str(n))))
  
# 참고 풀이 2. 배열 인덱싱을 이용한 풀이
def digit_reverse(n):
    return [int(i) for i in str(n)][::-1]
