from collections import Counter
n = int(input())
s = input().strip()


if n == 1:
    print('Yes')
else:
    count = Counter(s)
    print('Yes' if any(v >1 for v in count.values()) else 'No')