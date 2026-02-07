def printMinSteps(testcases):
    for testcase in testcases:
        last_year_present = False
        new_year_present = False
        last_year = []
        
        for char in testcase:
            if char == "2":
                if last_year:
                    if last_year[-1] != "0":
                        last_year = []

                last_year.append(char)

            elif char == "0" and last_year and last_year[-1] == "2":
                last_year.append(char)

            elif char == "5" and len(last_year) == 3 and last_year[-1] == "2":
                last_year_present = True
                last_year = []

            elif char == "6" and len(last_year) == 3 and last_year[-1] == "2":
                new_year_present = True
                break

            else:
                last_year = []

        if new_year_present:
            print(0)
        elif last_year_present:
            print(1)
        else:
            print(0)

if "__main__":
    n = int(input())
    testcases = []
    while n > 0:
        chars_len = int(input())
        chars = input()
        testcases.append(chars)
        n -= 1

    printMinSteps(testcases)