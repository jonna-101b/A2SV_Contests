if __name__ == "__main__":
    no_of_testcases = int(input())

    for _ in range(no_of_testcases):
        m, p_sum = [int(num) for num in input().split()]
        p = [int(num) for num in input().split()]
        p.sort()
        p_len = p[-1]
        i = 1
        index = 0
        printed = False

        while p_sum > 0:
            if index < len(p):
                if p[index] != i:
                    p_sum -= i
                    index -= 1 if i != 1 else 0
            else:
                p_sum -= i
 
            if p_sum < 0:
                print("NO")
                printed = True
            if p_sum == 0 and index >= len(p):
                print("YES")
                printed = True
            i += 1
            index += 1
        
        if index < len(p) and p_sum == 0:
            for j in range(index, len(p)):
                if p[j] != i:
                    p_sum -= p[j]

                if p_sum < 0:
                    print("NO")
                    printed = True
        
        if not printed:
            if p_sum < 0:
                print("NO")
            elif p_sum == 0:
                print("YES")