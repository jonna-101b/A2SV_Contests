from collections import defaultdict

if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        n, k = map(int, input().split())

        cost_dict = defaultdict(int)

        for _ in range(k):
            b, c = map(int, input().split())
            cost_dict[b] += c

        costs = sorted(cost_dict.values(), reverse=True)

        print(sum(costs[:n]))
