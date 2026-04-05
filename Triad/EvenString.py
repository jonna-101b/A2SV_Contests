if __name__ == "__main__":
    no_of_testcases = int(input())

    for _ in range(no_of_testcases):
        s = input().strip()
        count = 0
        delete = 0
        prev = None

        for char in s:
            if prev is None or char == prev:
                count += 1

            else:
                if count % 2 != 0:
                    delete += 1
                    count = 1

            prev = char

        print(delete)