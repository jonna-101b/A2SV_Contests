def solve(n, m, board):
    visted = [[False]*m for _ in range(n)]
    
    def DFS(r, c, pr, pc, color):
        if visted[r][c]:
            return True
            
        visted[r][c] = True
        dxn = [(1, 0), (-1, 0), (0, 1), (0 ,-1)]
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            
            if 0 <= nr < n and 0 <= nc < m:
                if board[nr][nc] != color:
                    continue
                
            if nr == pr and nc == pc:
                continue
            
            if DFS(nr, nc, r, c, color):
                return True
                
        return False
 
    for i in range(n):
        for j in range(m):
            if not visted[i][j]:
                if DFS(i, j, -1, -1, board[i][j]):
                    return "YES"
                
    return "NO"
 
if __name__ == "__main__":
    n, m = list(map(int, input().split()))
    board = [ input().strip().split() for _ in range(n) ]
    print(solve(n, m, board))
