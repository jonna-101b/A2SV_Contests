if __name__ == "__main__":
    no_of_testcases = int(input())

    for _ in range(no_of_testcases):
        n, l, r = [ int(num) for num in input().strip().split() ]
        cards = [ int(num) for num in input().strip().split() ]
        cards_sum = 0
        wins = 0

        for card in cards:
            cards_sum += card

            if l <= cards_sum <= r:
                wins += 1
                cards_sum = 0

            elif cards_sum > r:
                cards_sum = 0

        print(wins)