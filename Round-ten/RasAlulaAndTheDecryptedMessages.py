if __name__ == "__main__":
    no_of_testcases = int(input())
    
    for _ in range(no_of_testcases):
        n, m = map(int, input().split())
        s = input().strip()
        w = input().strip()
        target = sum(ord(c) for c in w)
        curr = sum(ord(c) for c in s[:m])
        found = (curr == target)
        
        for i in range(m, n):
            curr += ord(s[i])
            curr -= ord(s[i - m])
            
            if curr == target:
                found = True
                break
        
        if found:
            print("YES")
        else:
            print("NO")