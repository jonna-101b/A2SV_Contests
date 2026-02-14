tc = int(input())
for i in range(tc):
    cards = int(input())
    alice_white = 0
    alice_black = 0
    bob_white = 0
    bob_black = 0
    i = 1
    pos = 1
    while cards > 0:
        give = min(i, cards)
        if pos % 2 == 1:
            white = (give + 1) // 2
            black = give // 2
        else:
            black = (give + 1) // 2
            white = give // 2
        if i % 4 == 1 or i % 4 == 0:
            alice_white += white
            alice_black += black
        else:
            bob_white += white
            bob_black += black
        cards -= give
        pos += give
        i += 1
        
       
        
        
    print(alice_white, alice_black, bob_white, bob_black )
