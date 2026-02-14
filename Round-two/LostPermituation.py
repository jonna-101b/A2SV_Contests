t = int(input())

for _ in range(t):
    m, s = map(int, input().split())
    b = list(map(int, input().split()))
    
    sum_b = sum(b)
    total = sum_b + s
    
    n = 0
    found_n = False
    
    
    for i in range(1, 1000):
        if i * (i + 1) // 2 == total:
            n = i
            found_n = True
            break
    
    if not found_n:
        print("NO")
        continue
    
    if len(set(b)) != m or any(x > n for x in b):
        print("NO")
        continue
    
    print("YES")
