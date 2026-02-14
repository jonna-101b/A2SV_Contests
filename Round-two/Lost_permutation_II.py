if __name__ == "__main__":
    no_of_testcases = int(input())

    for _ in range(no_of_testcases):
        m, s = [int(num) for num in input().strip().split()]
        b = [int(num) for num in input().strip().split()]
        b.sort()
        counter = 1
        printed = False

        for i in range(m):
            if b[i] != counter:
                while counter < b[i]:
                    s -= counter
                    counter += 1

                if s < 0:
                    print("NO")
                    printed = True
                    break

            counter += 1

        if not printed:
            if s > 0:
                while s > 0:
                    if s >= counter:
                        s -= counter
                        counter += 1
                    else:
                        print("NO")
                        printed = True
                        break
                
                if not printed: print("YES")
            else:
                print("YES")