import sys

input = sys.stdin.readline
n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
"""
dfs로 3칸가면 ㅗ 제외한 테트로미노 모두 확인 가능
ㅗ는 dfs로 한칸 가면, 원래 위치에서 다시 dfs해줘야만 확인 가능
"""
def dfs(i, j, curSum, cnt):
    global maxVal
    if cnt == 4: # 3칸 채워져서 maxVal업데이트되고 리턴
        maxVal = max(maxVal, curSum)
        return
    
    for k in range(4):
        newR = i + dr[k]
        newC = j + dc[k]
        if 0 <= newR < n and 0 <= newC < m and not visited[newR][newC]:
            if cnt == 2: # ㅗ모양 탐색시 한칸 탐색하면 원래위치에서 재탐색해줘야 함
                visited[newR][newC] = True
                dfs(i, j, curSum + graph[newR][newC], cnt + 1)
                visited[newR][newC] = False

            # ㅗ 제외한 일반 모양 탐색
            visited[newR][newC] = True
            dfs(newR, newC, curSum + graph[newR][newC], cnt + 1)
            visited[newR][newC] = False


maxVal = -sys.maxsize - 1
visited = [[False] * m for _ in range(n)]
""" 시간복잡도 O(N*M * (dfs시간복잡도) ) 
    dfs는 4개의 인접한 노드를 방문하며, 이때 깊이가 3이므로 
    O(4 ^ 3)이다. 
    => O(N*M * (4^3))??
"""
for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(i, j, graph[i][j], 1)
        visited[i][j] = False


print(maxVal)
