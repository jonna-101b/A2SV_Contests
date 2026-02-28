if __name__ == "__main__":
    n, k = [ int(num) for num in input().strip().split() ]
    instruments = [ [i, int(num)] for i, num in enumerate(input().strip().split()) ]
    instruments.sort(key = lambda x: x[1])
    days = 0
    counter = 0
    indicies = []

    for i, instrument in instruments:
        days += instrument

        if days > k:
            break

        counter += 1
        indicies.append(i + 1)

    if counter:
        print(counter)
        print(*indicies)