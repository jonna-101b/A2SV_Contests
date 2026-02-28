tc = int(input())
for _ in range(tc):
    n, l, r = map(int, input().split())
    arr = list(map(int, input().split()))
    left = 0
    current_sum = 0
    wins = 0
    for right in range(n):
        current_sum += arr[right]
        while current_sum > r and left <= right:
            current_sum -= arr[left]
            left += 1
        if l <= current_sum <= r:
            wins += 1
            current_sum = 0
            left = right + 1
    print (wins)
