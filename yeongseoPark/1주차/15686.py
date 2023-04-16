import sys
input = sys.stdin.readline

n, m = map(int, input().split()) # 크기가 n*n도시, m은 폐업시키지 않을 최대 치킨집 개수

""" 입력받으면서 집과 치킨집을 리스트에 따로 기록 """
city  = [] 
chick = []
house = []
for i in range(n): 
    lst = list(map(int, input().split()))
    for j in range(n):
        if lst[j] == 1:
            house.append((i, j))
        
        elif lst[j] == 2: 
            chick.append((i, j))
    city.append(lst)

""" 치킨 거리 계산 """
def compute(one, two):
    return abs(one[0] - two[0]) + abs(one[1] - two[1])

ans = sys.maxsize
chosen_chick = [] # 폐업하지 않기로한 치킨집

""" 시간복잡도
- 백트래킹 조합 구하기 : O(C(치킨집개수, m)) = O(min(치킨집개수^m, 치킨집개수^(치킨집개수 - m))) : 11C3과 11C8중 연산 적은것 - 여기서는 11C3이 연산 더 적다
-> 이러면 최대 13C6 = 500만
- 위에다가 O(h * m) 곱한것 
= O(C(number of 치킨집 , m) * O(h, m))
"""
def dfs(depth, idx):
    global ans

    if depth == m: # 최대한 많이 골라야 도시의 치킨거리가 최소가 될 테니깐 m일때만 도시의 치킨거리 확인하면 됨
        sum = 0 
        """ 시간 복잡도 O(h * m) 이때 h는 n^2보다는 작은 값 """
        for h in house: # 각 집에서
            val = sys.maxsize
            for c in chosen_chick: # 현재 선택된 각 치킨집까지 가는 거리를 구해서
                tmp = compute(h, c)
                val = min(tmp, val) # 각 집의 치킨거리를 업데이트
            sum += val # 도시의 치킨거리에 각 집의 치킨거리 더해줌

        ans = min(ans, sum) # 도시의 치킨거리 업데이트
        return

    """ 조합의 백트래킹 구현 """
    for i in range(idx, len(chick)): 
        chosen_chick.append(chick[i])
        dfs(depth + 1, i + 1) 
        chosen_chick.pop() # 탐색을 마친후에는 제거해줌(m이 5면은 1,2,3,4,5 -> 1,2,3,4,6...)

dfs(0, 0)
print(ans)
    
