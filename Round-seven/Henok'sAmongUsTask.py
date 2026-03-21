from math import log2

if __name__ == "__main__":
    a, b = [ int(num) for num in input().strip().split() ]
    path = []
    
    while b >= a:
        path.append(b)

        if b == a:
            print("YES")
            path.reverse()
            print(len(path))
            print(*path)
            break

        if b % 10 == 1:
            b //= 10
        elif b % 2 == 0:
            b //= 2
        else:
            print("NO")
            break
    else:
        print("NO")