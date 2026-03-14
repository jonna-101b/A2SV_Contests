t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    freq = {}
    ans = 0
    
    for i in range(n):
        key = a[i] - (i + 1)
        freq[key] = freq.get(key, 0) + 1
        ans = max(ans, freq[key])
        
    print(ans)