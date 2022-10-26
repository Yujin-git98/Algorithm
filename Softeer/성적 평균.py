# 성적 평균
# N명의 학생들의 성적이 학번순서대로 주어졌다.
# 학번 구간 [A, B]가 주어졌을 때 이 학생들 성적의 평균을 구하는 프로그램을 작성하라

n, k = map(int, input().split()) # 학생수 n, 구간 수 k
stu = list(map(int, input().split())) # 학생 성적
ab=[]
for _ in range(k):
    a, b = map(int, input().split())
    ab.append([a-1,b-1]) # 학번 구간이 1부터 시작하니까



for _ in range(k):
    cnt = 0
    sum = 0
    a, b = ab.pop(0)
    for i in range(a, b+1):
        sum+=stu[i]
        cnt+=1
    print(round(sum/cnt, 2))
