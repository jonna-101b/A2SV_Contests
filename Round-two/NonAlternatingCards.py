if __name__ == "__main__":
    no_of_testcases = int(input())

    for _ in range(no_of_testcases):
        no_of_cards = int(input())
        alice_cards = 0
        bob_cards = 0
        counter = 1
        check = 1
        turn = 0

        while no_of_cards:
            if turn == 0:
                alice_cards += counter if counter < no_of_cards else no_of_cards
            else:
                bob_cards += counter if counter < no_of_cards else no_of_cards
            
            no_of_cards -= counter
            counter += 1
            check += 1
            if check == 2:
                check = 0
                turn = 1 - turn

        print(alice_cards, bob_cards)