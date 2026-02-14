tc = int(input())

for _ in range(tc):
    num = input()
    for i in range(len(num)):
        if num[i] != "0":
            n1 = num[i:]
            n2 = num[:i]
            if n1 and n2 and int(n1) > int(n2):
                print(num[:i], num[i:])
                break
    else:
        print(-1)
