n, B = map(int, input().split())
a = list(map(int, input().split()))

even = 0
odd = 0
costs = []

for i in range(n - 1):
    if a[i] % 2 == 0:
        even += 1
    else:
        odd += 1

    if even == odd:
        costs.append(abs(a[i] - a[i+1]))

costs.sort()

cuts = 0
spent = 0

for c in costs:
    if spent + c <= B:
        spent += c
        cuts += 1
    else:
        break

print(cuts)