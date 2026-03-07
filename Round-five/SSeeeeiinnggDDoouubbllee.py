if __name__ == "__main__":
    no_of_testcases = int(input())

    for _ in range(no_of_testcases):
        string = input().strip()
        palindrome = []
        i = 0

        while i < len(string):
            palindrome.append(string[i])
            i += 1

        i -= 1
        while i >= 0:
            palindrome.append(string[i])
            i -= 1

        print("".join(palindrome))