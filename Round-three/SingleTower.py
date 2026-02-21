if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    n = int(input())
    towers = []
    all_blocks = []

    for _ in range(n):
        data = list(map(int, input().split()))
        k = data[0]
        blocks = data[1:]
        towers.append(blocks)
        all_blocks.extend(blocks)

    # Step 1: sort all blocks
    sorted_blocks = sorted(all_blocks)

    # Step 2: map value -> position in sorted order
    position = {value: i for i, value in enumerate(sorted_blocks)}

    total_segments = 0

    # Step 3: count segments in each tower
    for tower in towers:
        total_segments += 1  # every tower contributes at least one segment

        for i in range(len(tower) - 1):
            if position[tower[i+1]] != position[tower[i]] + 1:
                total_segments += 1

    splits = total_segments - n
    combines = total_segments - 1

    print(splits, combines)