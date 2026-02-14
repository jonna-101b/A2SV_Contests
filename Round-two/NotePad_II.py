if __name__ == "__main__":
    no_of_testcases = int(input())

    for _ in range(no_of_testcases):
        n = int(input())
        s = input().strip()
        occurred = set()
        pair = ""
        last_pair = ""
        printed = False

        for char in s:
            pair += char
            pair = pair[1:] if len(pair) > 2 else pair

            if len(pair) == 2:
                if pair == last_pair:
                    last_pair = ""
                    continue
                
                elif pair in occurred:
                    print("YES")
                    printed  = True
                    break

                occurred.add(pair)
                last_pair = pair

        if not printed:
            print("NO")