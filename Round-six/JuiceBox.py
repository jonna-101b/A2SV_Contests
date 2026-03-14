from collections import defaultdict

if __name__ == "__main__":
    no_of_testcases = int(input())

    for _ in range(no_of_testcases):
        n, k = [ int(num) for num in input().strip().split() ]
        cost_dict = defaultdict(int)

        for _ in range(k):
            brand, cost = [ int(num) for num in input().strip().split() ]
            cost_dict[brand] += cost

        cost_list = [ (brand, cost_dict[brand]) for brand in cost_dict ]
        cost_list.sort(reverse = True, key = lambda x: x[1])
        max_cost = 0

        for i in range(min(n, len(cost_list))):
            max_cost += cost_list[i][1]

        print(max_cost)