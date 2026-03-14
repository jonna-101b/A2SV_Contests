from collections import defaultdict

if __name__ == "__main__":
    no_of_testcases = int(input())

    for _ in range(no_of_testcases):
        n = int(input())
        nums = [ int(num) for num in input().strip().split() ]
        nums.sort()
        diff = defaultdict(int)

        for i in range(len(nums) - 1):
            difference = nums[i+1] - nums[i]
            if difference:
                diff[difference] += 1

        max_nums = 1
        for difference in diff:
            minimum = n//difference if n//difference > 1 else (2 if n//difference == 1 else 0)
            actual = min(minimum, diff[difference] + 1)
            max_nums = max(max_nums, actual)

        print(max_nums)