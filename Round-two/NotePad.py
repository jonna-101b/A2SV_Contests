def solve():
    n = int(input())
    s = input().strip()
    
    seen = {}
    for i in range(n - 1):
        pair = s[i:i+2]
        if pair in seen:
            
            if seen[pair] < i - 1:
                print("YES")
                return
        else:
            seen[pair] = i
    print("NO")

t = int(input())
for _ in range(t):
    solve()
