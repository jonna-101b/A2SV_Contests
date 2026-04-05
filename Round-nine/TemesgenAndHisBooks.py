tc = int(input())
for _ in range(tc):
    n = int(input())
    pages = list(map(int, input().split()))

    pile1 = pages[-1]
    pile2 = max(pages[:-1])
    print(pile1 + pile2)