if __name__ == "__main__":
    n, k = [ int(num) for num in input().strip().split() ]
    h = [ [i, int(num)] for i, num in enumerate(input().strip().split()) ]
    h.sort(key=lambda x: x[1])
    maximum = []
    counter = 0
    prev = None
    last = 0

    for height in h:
        if prev is None or height - prev < k:
            counter += 1
        else:
            counter = 0
            last = 

        if len(maximum) == 0 and counter > maximum[1] - maximum[0] + 1:
            maximum = [last, i]