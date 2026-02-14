from random import choose

# Best time case implementation (AKA Jonna implementation)

def jonnas_implementation():
    if "__main__":
        list_length = int(input())
        numbers = list(map(int, input().split()))

        no_copy = numbers.copy()
        no_copy.sort(reverse = True)
        ranks = dict()
        last_num = None
        frequency = 0
        for num in no_copy:
            if last_num is None:
                ranks[num] = 1
            elif num != last_num:
                ranks[num] = ranks[last_num] + 1 + frequency
                frequency = 0
            else:
                frequency += 1
            
            last_num = num

        res = []
        for num in numbers:
            res.append(ranks[num])

        print(*res)
        print("Jonna's Implementation")

# Kaleab's Implementation

def kaleab_implementation():
    tc = int(input())
    ranks = []
    nums = list(map(int, input().split()))
    for i in range(len(nums)):
        ranks.append(1 + len([x for x in nums if x > nums[i]]))
    print(*ranks)

    print("Kaleab's Implementation")

choose([jonnas_implementation, kaleab_implementation])()