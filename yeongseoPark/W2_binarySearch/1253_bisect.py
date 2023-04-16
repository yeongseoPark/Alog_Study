import sys
input = sys.stdin.readline

n, h = map(int, input().split())

down = []
up   = []
for i in range(n):
    if i % 2 == 0: # 석순
        down.append(int(input()))
    else:          # 종유석
        up.append(int(input()))

down.sort()
up.sort()

""" 
bisect_left(a,x) :
a[:i] 가 x보다 작은 i 중, 제일 큰 i 값을 반환
"""
def bisect_left(array, target):
    start = 0
    end   = len(array)
    while start < end:
        mid = (start + end) // 2

        if array[mid] < target:
            start = mid + 1
        else:
            end = mid
    
    return start

"""
bisect_right(a,x): a[:i]가 x보다 작거나 같은 i 중 제일큰 i를 반환
"""
def bisect_right(arr, target):
    lo = 0
    hi = len(arr)
    while lo < hi:
        mid = (lo+hi) // 2
        if arr[mid] <= target:
            lo = mid + 1
        else:
            hi = mid
    
    return lo

minVal = sys.maxsize
cnt = 1
for i in range(1, h+1): # 각 구간에 존재하지 않는(거기까지 미치지 않는 - bisect left로 정렬된 배열에서 그 이전값의 개수를 구함)
    t, b = bisect_left(up, (h+1) - i), bisect_left(down, i)  # 종유석의 개수와 석순의 개수를 구함

    total = n - (t+b) # 이 둘을 더해서 전체 길이에서 빼면, 장애물의 개수

    if total < minVal: # 장애물의 개수가 기존 최소값보다 작으면 업데이트
        minVal = total
        cnt = 1

    elif total == minVal: # 장애물의 개수가 기존 최소값만큼이면 구간의 수 += 1
        cnt += 1

print(minVal, cnt)








""" 구간에서의 장애물 개수 기록(이중포문)하고, 이를 정렬해서 min값 구한 이후, min값이 몇개 나오는지 이분탐색으로 확인 -> 시간초과 """
# obs = [0] * (h+1) # 특 정 구간에서의 장애물 개수 기록(구간 = 높이)

# # 구간 k에서의 총 장애물 개수 기록
# # 이중포문 -> O(N*H) 시간초과
# for i in range(n):
#     tmp = int(input())
#     if i % 2 == 1: # 홀수면(종유석이면)
#         for j in range(h-tmp+1, h+1):
#             obs[j] += 1

#     else: # 석순이면
#         for j in range(1, tmp+1):
#             obs[j] += 1

# obs.sort() # 오름차순 정렬
# minVal = obs[1]
# cnt = 0 # 장애물의 최솟값이 나오는 구간의 수 

# # obj안에서 min값이 몇개있는지 이분탐색으로 찾음
# lo = 1
# hi = h

# while lo < hi:
#     mid = (lo+hi) // 2

#     if obs[mid] > minVal:
#         hi = mid - 1

#     elif obs[mid] <= minVal:
#         lo = mid + 1

# cnt = hi

# print(minVal, cnt, sep=" ")