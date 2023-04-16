import sys
input = sys.stdin.readline

n = int(input())

bud = list(map(int, input().split()))

m = int(input())

cutted = False

# 예산 계산
def compute(std):
    curbud = 0

    for i in bud:
        if i >= std:
            curbud += std
        else:
            curbud += i
    
    return curbud

lo = 1
hi = m # 상한선은 아무리 많아도 총 예산 m
setted = False

while lo < hi:
    mid = (lo + hi) // 2  # 예산 상한액

    curbudget = compute(mid)

    if curbudget < m:
        lo = mid + 1
    
    elif curbudget > m:
        hi = mid - 1
    
    else:
        setted= True
        break

if setted: # 딱 현재 상한선에서 m에 들어맞는 경우
    print(min(mid, max(bud)))
    exit()

# 현재 상한선에서 m보다 살짝 모자르지만, 이게 최대 상한선
print(min(hi, max(bud))) # 왜 lo로 하면 안됨???
