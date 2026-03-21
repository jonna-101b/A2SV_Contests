import sys
sys.setrecursionlimit(10**7)

if __name__ == "__main__":
    no_of_testcases = int(input())

    for _ in range(no_of_testcases):
        n, m = [ int(num) for num in input().strip().split() ]

        def check(n = n, m = m):
            if n == m:
                return True
            
            if n % 3 != 0 or m > n:
                return False
            
            one = n // 3
            two = one * 2
            if one == m or two == m:
                return True
            
            return check(one) or check(two)
        
        print("YES" if check() else "NO")