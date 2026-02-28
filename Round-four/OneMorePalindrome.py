if __name__ == "__main__":
    no_of_testcases = int(input())

    for _ in range(no_of_testcases):
        s = input().strip()
        i, j = 0, len(s) - 1
        last = None
        printed = False

        while i < j:
            if last is not None and s[i] != last:
                print("YES")
                printed = True
                break

            last = s[i]
            i += 1
            j -= 1

        if not printed:
            print("NO")