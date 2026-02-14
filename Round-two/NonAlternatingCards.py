tc = int(input())
for i in range(tc):
    cards = int(input())
    alice = 0
    bob = 0
    i = 1
    while cards > 0:
        give = min(i, cards)
        if i % 4 == 1 or i % 4 == 0:
            alice += give
        else:
            bob += give
        cards -= give
        i += 1
    print(alice, bob)
