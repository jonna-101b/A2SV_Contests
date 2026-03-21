if __name__ == "__main__":
    n = int(input().strip())
    s = input()
    counter = 1
    delete = 0
    res = []

    for i, char in enumerate(s):
        if counter % 2 == 0:
            if res and s[i] == res[-1]:
                delete += 1
            else:
                res.append(char)
                counter += 1
        else:
            res.append(char)
            counter += 1

    if len(res) % 2 != 0:
        res.pop()
        delete += 1

    print(delete)
    print("".join(res))