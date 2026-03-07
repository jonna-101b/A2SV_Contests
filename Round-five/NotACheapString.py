if __name__ == "main":
    no_of_testcases = int(input())

    for _ in range(no_of_testcases):
        order = { chr(i): i - ord("a") + 1 for i in range(ord("a"), ord("z") + 1) }
        string = input().strip()
        p = int(input())
        w = []
        sorted_w = []
        price = 0

        for char in string:
            price += order[char]
            w.append((char, False))
            sorted_w.append(char)

        if price <= p:
            print("".join([ char for char, deleted in w ]))

        else:
            sorted_w.sort(reverse = True)
            i = 0

            while price > p:
                for j in range(len(w)):
                    if w[j][0] == sorted_w[i]:
                        w[j][1] = True
                        price -= order[w[j][0]]
                        break

                i += 1

            print("".join([ char for char, deleted in w if deleted == False ]))
