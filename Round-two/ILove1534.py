def solve():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        grid = [input().strip() for _ in range(n)]
        
        total = 0
        layers = min(n, m) // 2
        
        for k in range(layers):
            top = k
            bottom = n - k - 1
            left = k
            right = m - k - 1
            
            layer = []
            
            # top row
            for j in range(left, right + 1):
                layer.append(grid[top][j])
            
            # right column
            for i in range(top + 1, bottom):
                layer.append(grid[i][right])
            
            # bottom row
            for j in range(right, left - 1, -1):
                layer.append(grid[bottom][j])
            
            # left column
            for i in range(bottom - 1, top, -1):
                layer.append(grid[i][left])
            
            layer_str = "".join(layer)
            
            # make it circular
            layer_str += layer_str[:3]
            
            # count occurrences
            for i in range(len(layer)):
                if layer_str[i:i+4] == "1543":
                    total += 1
        
        print(total)

solve()