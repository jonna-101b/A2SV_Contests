if __name__ == "__main__":
    no_of_testcases = int(input())
    
    for _ in range(no_of_testcases):
        cards = int(input())
        alice = 0
        bob = 0
        isAlice = True
        counter = 1
        steps = 1

        while cards > 0:
            if isAlice:
                alice += counter if counter < cards else cards
            else:
                bob += counter if counter < cards else cards

            cards -= counter
            steps += 1
            counter += 1
            if steps == 2:
                steps = 0
                isAlice = not isAlice

        print(alice, bob)