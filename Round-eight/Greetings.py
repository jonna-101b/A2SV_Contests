if __name__ == "__main__":
    no_of_testcases = int(input())

    for _ in range(no_of_testcases):
        n = int(input())
        journey = [ [ int(num) for num in input().strip().split() ] for _ in range(n) ]
        counter = 0
        greetings = 0

        while counter <= n:
            present = 0
            for start, end in journey:
                pass