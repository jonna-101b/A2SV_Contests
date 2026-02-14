if __name__ == "__main__":
    no_of_testcases = int(input())
    
    for _ in range(no_of_testcases):
        cards = int(input())
        alice_w = 0
        alice_b = 0
        bob_w = 0
        bob_b = 0
        isAlice = True
        last_count = 0
        curr_count = 1
        counter = 1
        steps = 1

        while cards > 0:
            if isAlice:
                if last_count == 0:
                    alice_w += 1

                else:
                    start = last_count
                    end = curr_count + 1 if counter < cards else last_count + cards
                    for i in range(start, end):
                        if i % 2 == 0:
                            alice_b += 1
                        else:
                            alice_w += 1
            else:
                if last_count == 0:
                    bob_w += 1

                else:
                    start = last_count
                    end = curr_count + 1 if counter < cards else last_count + cards
                    for i in range(start, end):
                        if i % 2 == 0:
                            bob_b += 1
                        else:
                            bob_w += 1

            cards -= counter
            steps += 1
            counter += 1
            last_count = curr_count + 1
            curr_count += counter
            if steps == 2:
                steps = 0
                isAlice = not isAlice

        print(alice_w, alice_b, bob_w, bob_b)