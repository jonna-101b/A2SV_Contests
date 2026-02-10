from collections import Counter

def checkOrder(s, t):
    start = 0
    for char in s:
        pos = t.find(char, start)
        if pos == -1:
            print("NO")
            return False

        else:
            start = pos

    return True

if "__main__":
    no_of_testcases = int(input())

    for _ in range(no_of_testcases):
        s = input()
        t = input()
        p = input()

        order = checkOrder(s, t)
        if order:
            sp = Counter(s+p)
            
            for char in t:
                if sp.get(char, 0) <= 0:
                    print("NO")
                    break
                
                sp[char] -= 1
            else:
                print("YES")