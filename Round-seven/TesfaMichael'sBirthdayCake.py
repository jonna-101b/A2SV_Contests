if __name__ == "__main__":
    n, k = [ int(num) for num in input().strip().split() ]
    layers = sorted(input().strip())
    weight = 0
    prev = None

    for letter in layers:
        if k == 0:
            break

        if prev is not None:
            if ord(letter) - ord(prev) > 1:
                weight += ord(letter) - ord("a") + 1
                k -= 1
        else:
            weight += ord(letter) - ord("a") + 1
            k -= 1

        prev = letter

    if k > 0:
        print(-1)
    else:
        print(weight)





# B. TesfaMichael's Birthday Cake
# time limit per test1 s.
# memory limit per test256 MB
# Today is TesfaMichael's birthday! To celebrate, he is going to bake a massive birthday cake, which consists of several layers in some order. Each of the layers is defined by a lowercase Latin letter. This way, the cake can be described by the string — concatenation of letters, which correspond to the layers.

# There are n
#  layers available. The cake must contain exactly k
#  of them. Layers in the cake should be ordered by their weight. So, after the layer with some letter can go only layer with a letter, which is at least two positions after in the alphabet (skipping one letter in between, or even more). For example, after letter 'c' can't go letters 'a', 'b', 'c' and 'd', but can go letters 'e', 'f', ..., 'z'.

# For the cake to be easily carried to the party, its weight should be minimal. The weight of the cake is equal to the sum of the weights of its layers. The weight of the layer is the number of its letter in the alphabet. For example, the layer 'a 'weighs one gram,' b 'weighs two grams, and' z' — 26
#  grams.

# Build the cake with the minimal weight or determine, that it is impossible to build a cake at all. Each layer can be used at most once.

# Input
# The first line of input contains two integers — n
#  and k
#  (1≤k≤n≤50
# ) – the number of available layers and the number of layers to use in the cake.

# The second line contains string s
# , which consists of exactly n
#  lowercase Latin letters. Each letter defines a new layer, which can be used to build the cake. Each layer can be used at most once.

# Output
# Print a single integer — the minimal total weight of the cake or -1, if it is impossible to build the cake at all.