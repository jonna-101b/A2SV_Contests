from collections import Counter

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    arr = [ int(num) for num in input().strip().split() ]

    freq = Counter(arr)
    values = sorted(freq.keys())

    left = 0
    current_sum = 0
    distinct = 0
    max_cards = 0

    for right in range(len(values)):
        current_sum += freq[values[right]]
        distinct += 1

        while distinct > k:
            current_sum -= freq[values[left]]
            distinct -= 1
            left += 1

        max_cards = max(max_cards, current_sum)

    print(max_cards)
