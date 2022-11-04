# 백준 10825번 국영수
# 학생 N명의 이름과 국, 영, 수 점수가 주어짐.
# 다음과 같은 조건으로 학생의 성적을 정렬하는 프로그램을 작성해라
# 1. 국어 점수가 감소하는 순서로
# 2. 국어점수가 같으면 영어 점수가 증가하는 순서로
# 3. 국어 점수와 영어 점수가 같으면 수학 점수가 감소하는 순서로
# 4. 모든 점수가 같으면 이름이 사전 순으로 증가하는 순서로

n=int(input()) # n명의 학생
students=[]
for _ in range(n):
    s, a, b, c=input().split()
    students.append([s, int(a), int(b), int(c)])
#print(students)
students.sort(key=lambda x:(-x[1], x[2], -x[3], x[0]))
for s in students:
    print(s[0])
