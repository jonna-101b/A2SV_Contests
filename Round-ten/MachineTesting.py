from math import ceil

if __name__ == "__main__":
    no_of_testcases = int(input())

    for _ in range(no_of_testcases):
        n = int(input())
        h = list(map(int, input().split()))
        p = list(map(int, input().split()))
        total = 0
        permitted = [None]

        for i in range(len(h)-1):
            time = 0
            if len(permitted) == 1:
                time = ceil(h[i+1] / p[i])
                permitted.append(time)
                total += time
            else:
                health = h[i+1]
                counter = i
                while health > 0:
                    if permitted[counter] is None or counter == 0:
                        time += ceil(health / p[counter])
                        health = 0
                    else:
                        time += permitted[counter] if health >= permitted[counter] * p[counter] else ceil(health / p[counter])
                        health -= permitted[counter] * p[counter]
                        counter -= 1

                permitted.append(time)
                if time > total:
                    total += time - total

        print(total)
