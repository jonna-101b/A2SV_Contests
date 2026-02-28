if __name__ == "__main__":
    no_of_testcases = int(input())

    for _ in range(no_of_testcases):
        n = int(input())
        nums = [ int(num) for num in input().strip().split() ]
        nums.sort()
        i = 0
        score = 0

        while i < 2*n:
            score += nums[i]
            i += 2

        print(score)