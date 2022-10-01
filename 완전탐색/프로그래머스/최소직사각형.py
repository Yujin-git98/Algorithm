# 참고 코드
# 가로 길이, 세로 길이 구분 없이 둘 중에서 큰것과 작은 것을 나눔.
# 그리고 전체에서 큰 것 중에 큰 것을 고르고 작은 것 중에 큰 것을 고름

def solution(sizes):

    answer=max(max(size) for size in sizes)*max(min(size) for size in sizes)
           
    return answer
