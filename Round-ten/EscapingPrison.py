if __name__ == "__main__":
    no_of_testcases = int(input())

    for _ in range(no_of_testcases):
        n, h = list(map(int, input().split()))

        for _ in range(n):
            h -= max(list(map(int, input().split())))

        if h <= 0: 
            print("YES")
        else:
            print("NO")