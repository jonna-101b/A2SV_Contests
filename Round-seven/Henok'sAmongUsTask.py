from math import log2

if __name__ == "__main__":
    a, b = [ int(num) for num in input().strip().split() ]
    last = b % 10
    target = b // 10
    printed = False
    
    while last and last != 1:
        if last % 2 != 0:
            printed = True
            break

        last = b % 10
        target = b // 10

    if printed:
        print("NO")
    else:
        var1 = target // 10
        if var1 % 1 == 0:
            steps = log2(var1)
            if log2(var1) % 1 == 0:
                print("Yes")

            else:
                print("NO")

        else:
            print("NO")










# C. Henok's Among Us Task
# time limit per test1 s.
# memory limit per test256 MB
# Henok is playing a relaxing game of Among Us with his students to celebrate everyone passing seventy percent progress on the Progress Sheet. He is currently playing as a Crewmate and is trying to finish his tasks.

# He is at the admin terminal trying to hack the system to complete a visual task. The terminal gives him a starting code a
# , which he needs to turn into the target override code b
# . For this purpose, he can push two buttons that do the following operations:

# multiply the current code by 2
#  (that is, replace the code x
#  by 2⋅x
# );
# append the digit 1
#  to the right of current code (that is, replace the code x
#  by 10⋅x+1
# ).
# You need to help Henok to transform the code a
#  into the code b
#  using only the operations described above, or find that it is impossible so he can run away before the Impostor finds him!

# Note that in this task you are not required to minimize the number of operations. It suffices to find any way to transform a
#  into b
# .

# Input
# The first line contains two positive integers a
#  and b
#  (1≤a<b≤109
# ) — the starting code which Henok has and the target override code he wants to reach.

# Output
# If there is no way to get b
#  from a
# , print "NO" (without quotes).

# Otherwise print three lines. On the first line print "YES" (without quotes). The second line should contain single integer k
#  — the length of the transformation sequence. On the third line print the sequence of transformations x1,x2,…,xk
# , where:

# x1
#  should be equal to a
# ,
# xk
#  should be equal to b
# ,
# xi
#  should be obtained from xi−1
#  using any of two described operations (1<i≤k
# ).
# If there are multiple answers, print any of them.