def solve(n, m, board):
    found = False
    
    def DFS(row, col, color):
        nonlocal found
        
        if row < 0 or row >= n:
            return 
        
        if col < 0 or col >= m:
            return
        
        if color is not None and board[row][col] != color:
            return
        
        if board[row][col] == "VISiTED":
            found = True
            return
            
        DFS(row+1, col)
        DFS(row-1, col)
        DFS(row, col+1)
        DFS(row, col-1)
        board[row][col] = "VISiTED"
        return

    for i in range(n):
        for j in range(m):
            if board[i][j] != "VISiTED":
                DFS(i, j)
                
            if found:
                return "YES"
                
    return "NO"

if __name__ == "__main__":
    n, m = list(map(int, input().split()))
    board = [ board.append(input().split()) for _ in range(n) ]
    print(solve(n, m, board))
    
    
