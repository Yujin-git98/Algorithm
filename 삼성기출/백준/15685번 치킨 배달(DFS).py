#15685번 치킨 배달
# nxn인 도시. 도시의 각 칸은 빈칸, 치킨집, 집 중 하나이다.
# 도시의 칸은 r행 c열이다. r과 c는 1부터 시작한다.
# 치킨 거리는 집과 가장 가까운 치킨집 사이의 거리이다.
# 각각의 집은 치킨 거리를 가지고 있다. 도시의 치킨 거리는 모든 집의 치킨 거리의 합이다.
# 도시에 있는 치킨집 중에서 최대 M개를 고르고 도시의 치킨 거리가 가장 작게 되도록 구현해라

n,m=map(int,input().split()) #nxn 도시. m개의 치킨집
graph=[list(map(int, input().split())) for _ in range(n)] # 0은 빈칸, 1은 집, 2는 치킨집

house_list = []
chicken_list = []
choosen_chicken_list = []
answer = 1000000 # 임의의 숫자
# 치킨집, 집 위치 값 넣기
for i in range(n):
    for j in range(n):
        if graph[i][j] == 2:
            chicken_list.append((i,j))
        if graph[i][j] == 1:
            house_list.append((i,j))
answer=100000

# 백트랙킹 문제는 dfs 자체를 특정 방향으로 구현하기 위한 조건(예를 들어 combination)이거나
# 문제에서 요구하는 return조건(탈출 조건)이 포인트이다.
def dfs(depth, idx):
    global answer
    if depth==m:
        sum=0
        for house in house_list:
            val=1000000
            for choosen_chicken in choosen_chicken_list:
                tmp=abs(house[0]-choosen_chicken[0])+abs(house[1]-choosen_chicken[1])
                val=min(tmp, val) # 각 house 당 치킨 거리의 최소 값 : val
            sum+=val #도시의 치킨 거리 : val의 합 : 각 house 당 치킨 거리의 최소 값의 합
        answer=min(answer, sum)
        return

    # combination구현 : idx를 인자로 넣어주어 인덱스보다 더 적은 값은 들어오지 못하게 했다.
    # 이미 같은 것을 가지고 있는 경우는 continue를 통해 중복을 제거하여 구현
    for i in range(idx, len(chicken_list)):
        if chicken_list[i] in choosen_chicken_list:
            continue
        choosen_chicken_list.append(chicken_list[i])
        dfs(depth+1, i+1)
        choosen_chicken_list.pop()
dfs(0, 0)
print(answer)
