tc = int(input())


def check_trailing(num):
    if num.startswith("0"):
        return False
    else:
        return True


for _ in range(tc):
    num = input()
    for i in range(len(num)):
        num1 = num[: i + 1]
        num2 = num[i + 1 :]
        if check_trailing(num1) and check_trailing(num2):
            num1 = int(num1)
            num2 = int(num2)
            if num2 > num1:
                print(num1, num2)
                break
