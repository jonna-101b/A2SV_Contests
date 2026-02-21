def checkMirrorCase(grid, i, j):
    if grid[i][j] != grid[j][i]: # 270 degree check
        return True
    # elif 

if __name__ == "__main__":
    no_of_testcases = int(input())

    for _ in range(no_of_testcases):
        size = int(input())
        grid = [[int(num) for num in input().strip()] for _ in range(size)]
        counter = 0

        for i in range(size):
            for j in range(i):
                if grid[i][j] != grid[j][i]:
                    counter += 1

        print(counter)