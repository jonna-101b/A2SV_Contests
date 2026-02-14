def clacBlack(start, end, counter):
    if counter % 2 == 0:
        return (end - start + 1) // 2
    else:  
        if start:
            if start % 2 == 0:
                return (end - start) // 2 + 1
            else:
                return (end - start) // 2
        else:
            return 0

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
            black = clacBlack(last_count, curr_count if counter < cards else last_count + cards - 1, counter)

            if isAlice:
                alice_w += counter - black if counter < cards else cards - black
                alice_b += black
            else:
                bob_w += counter - black if counter < cards else cards - black
                bob_b += black

            cards -= counter
            steps += 1
            counter += 1
            last_count = curr_count + 1
            curr_count += counter
            if steps == 2:
                steps = 0
                isAlice = not isAlice

        print(alice_w, alice_b, bob_w, bob_b)