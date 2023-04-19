n, m, l = map(int, input().split())

arr = [0] + list(map(int, input().split())) + [l]
arr.sort()

start = 1 # 도로의 시작 
end = l - 1 # 도로의 끝에서 한칸전

"""
가장 멀리 있는 휴게소 사이의 거리- 를 가지고 이분탐색 
O(n log L)
"""
while start <= end:
    count = 0              # 설치해야할 휴게소 개수
    mid = (start+end) // 2 # 휴게소가 없는 구간의 최댓값
    
    for i in range(1, len(arr)): # 현재 거리 중 mid보다 큰 거리를 찾아서
        if arr[i] - arr[i-1] > mid:
            # 현재의 거리에 mid를 기준으로 했을때, 총 몇개의 휴게소 설치 가능? 
            count += (arr[i] - arr[i-1] - 1) // mid
            # 이때 1빼주는 이유는, 현재 설치된 곳은 고려해주지 않아야 하기 때문
            # arr[i]= 5, arr[i] = 1로 놓고 생각해보면 됨
    
    # 가장 멀리 떨어져있는 휴게소 사이의 거리가 mid가 되게 설치를 해놓고 보니,
    if count > m: # 설치해야할 휴게소 개수가 m보다 크다면, mid는 더 길어야 한다
        start = mid + 1
    else:         # 설치해야할 휴게소 개수가 m보다 작거나 같으면, mid는 더 짧아야 한다
        end = mid - 1
        result = mid
        # 정답 : 휴게소 개수가 m보다 많아진 그 단계의 전 경우

print(result)
# print(end+1) 이것도 1654경우와 마찬가지로, start=end일시 end가 한칸더 줄어들것이므로 end에다 1더해준값 프린트해도 답임