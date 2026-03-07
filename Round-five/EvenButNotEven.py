if __name__ == "main":
    no_of_testcases = int(input())

    for _ in range(no_of_testcases):
        n = int(input())
        num = [digit for digit in input().strip()]

        while len(num) > 1 and int(num[-1]) % 2 == 0:
            num.pop()

        if len(num) == 1:
            print(-1)
        else:
            odd_count = 0
            odd = None

            for i in range(len(num)):
                if int(num[i]) % 2 != 0:
                    odd_count += 1
                    if i != len(num) - 1:
                        odd = i

            if odd_count % 2 == 0:
                print("".join(num))
            else:
                if odd is None:
                    print(-1)
                else:
                    print("".join(num[i] for i in range(len(num)) if i != odd))