# 참고 풀이1. 
# 이전 인덱스와 현재 인덱스가 다르면 새로운 배열에 추가
# 처음에 새로운 배열을 arr[0]으로 초기화 해줘야함.

def solution(arr):
    answer = [arr[0]]
    #queue=deque(arr)
    for i in range(1, len(arr)):
        if arr[i]!=arr[i-1]:
            answer.append(arr[i])
    return answer
  
# 참고 풀이2.
# 새로운 리스트의 맨 오른쪽 부분과 현재 리스트를 비교하여 같으면 다음 for문으로 넘어감
def no_continuous(s):
    a = []
    for i in s:
        if a[-1:] == [i]: continue
        a.append(i)
    return a
