from collections import deque

if __name__ == "__main__":
    no_of_testcases = int(input())

    for _ in range(no_of_testcases):
        n = int(input())
        s = input()
        new_s = deque(s)
        same = False

        while not same:
            stack = ["T", "M", "T"]
            for i in range(len(new_s)-1, -1, -1):
                if stack:
                    if new_s[i] == stack[-1]:
                        new_s.pop(i)

                else:
                    break