import sys
# sys.setrecursionlimit(10**7) -> 있으면 pypy에서 메모리초과

dp = [[[0] * 21 for _ in range(21)] for i in range(21)]

"""
dp가 없으면 O(2^n)이나, dp가 있어서
O(20^3) - 모든 가능한 경우- ??
"""

def re(a, b, c):
    if a <= 0 or b <= 0 or c <= 0: # 상위 조건 
        return 1
    
    if a > 20 or b > 20 or c > 20: # 상위 조건 2
        return re(20, 20, 20)
    
    if dp[a][b][c]: # 이미 계산한 값일경우 dp에 저장된 값 리턴
        return dp[a][b][c]

    if a < b and b < c:
        dp[a][b][c] = re(a, b, c-1) + re(a, b-1, c-1) - re(a, b-1, c) # 재귀함수 호출한 결과 dp테이블에 값 저장하고, 해당 값 리턴
        return dp[a][b][c]

    dp[a][b][c] = re(a-1, b, c) + re(a-1, b-1, c) + re(a-1, b, c-1) - re(a-1, b-1, c-1)
    return dp[a][b][c]


while True:
    a, b, c= map(int, sys.stdin.readline().split())

    if a == -1 and b == -1 and c == -1:
        break

    # if a > 20 or b > 20 or c > 20: => 여기서 처리해주면, 선행조건인 a <=0 b <= 0 c <= 0 을 먼저 처리해주지 못하기 때문에 틀림 
    #     a = 20
    #     b = 20
    #     c = 20

    res  = re(a, b, c)
        
    print(f'w({a}, {b}, {c}) = {res}')