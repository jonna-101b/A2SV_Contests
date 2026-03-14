n = int(input())
products = []

for _ in range(n):
    ai, bi = map(int, input().split())
    products.append([ai, bi])

    products.sort(key=lambda x: x[1])  # sort by bi

    i = 0
    j = n - 1
    total_bought = 0
    cost = 0

    while i <= j:
        if total_bought >= products[i][1]:
            # discount is active
            cost += products[i][0]
            total_bought += products[i][0]
            i += 1
        else:
            need = products[i][1] - total_bought
            take = min(need, products[j][0])
            cost += take * 2
            total_bought += take
            products[j][0] -= take
            if products[j][0] == 0:
                j -= 1

    print(cost)