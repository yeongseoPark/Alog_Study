import sys
input = sys.stdin.readline

k, n = map(int, input().split())

lan = []
maxVal = -sys.maxsize - 1
for _ in range(k):
    tmp = int(input())
    if tmp > maxVal:
        maxVal = tmp
    
    lan.append(tmp)

lan.sort(reverse=True) # 내림차순

def compute(cut):
    ans = 0 
    for i in lan:
        if i < cut: # cut보다 작으면 어차피 못만듬
            break
        ans += i // cut
    
    return ans

# 범위?
lo = 1
hi = maxVal # 제일 긴 랜선만 가지고도 n개만들수 있을지도 있자나

while lo <= hi: # = 안붙여주면 틀리는 이유..?
    # lo = hi일때, 만들 수 있는 개수가 적어서 한칸 줄여준거랑, 반대로 한칸 늘려준경우가 만남
    # 이 상태에서 lo에는 n개이상의 랜선만들수 있는 최대 길이가 저장됨
    # 여기서 mid를 구하면 다시 자기 자신의 값 mid가 나오므로, 무조건 lo가 한칸 앞으로 가게됨(else문에 걸리니까)
    # 그래서 한칸 앞으로 나간 lo에서 -1해준게 답이 되는거

    mid = (lo + hi) // 2

    count = compute(mid)

    if count < n: # 현재 만들수 있는 개수가 n보다 적으면, 랜선의 길이 줄여줘야 함
        hi = mid - 1 
    else:         # 현재 만들 수 있는 개수가 n보다 같거나 많으면, 랜선의 길이 늘릴 수 있음
        lo = mid + 1

print(lo-1)
# print(hi) 따라서 이것도 됨