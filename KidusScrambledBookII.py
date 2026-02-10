tc = int(input())

for _ in range(tc):
    num = input()
    for i in range(len(num)):
        if num[i] != 0 and int(num[i:]) > int(num[:i]):
            print(num[:i], num[i:])
            break
    else:
        print(-1)
