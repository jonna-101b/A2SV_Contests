def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = input().strip()
        
        seen = set()
        possible = False
        
        for i in range(n - 1):
            sub = s[i:i+2]
            if sub in seen:
                possible = True
                break
            seen.add(sub)
        
        print("YES" if possible else "NO")
