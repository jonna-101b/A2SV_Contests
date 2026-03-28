from collections import Counter

if __name__ == "__main__":
    n = int(input().strip())
    foods = input().strip()
    occurrence = Counter(foods)
    me = { "L": 0, "O": 0}
    friend = { "L": occurrence["L"], "O": occurrence["O"]}
    counter = 1
    found = False

    for food in foods:
        me[food] += 1
        friend[food] -= 1

        if me["L"] != friend["L"] and me["O"] != friend["O"] and (friend["L"] or friend["O"]):
            found = True
            break

        counter += 1

    if found:
        print(counter)
    else:
        print(-1)