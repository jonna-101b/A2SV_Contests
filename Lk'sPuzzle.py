def solve(n, m, board):
    visited = [[False]*m for _ in range(n)]
    
    def dfs(r, c, pr, pc, color):
        if visited[r][c]:
            return True
        
        visited[r][c] = True
        
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            
            if 0 <= nr < n and 0 <= nc < m:
                if board[nr][nc] != color:
                    continue
                
                # skip the parent cell
                if nr == pr and nc == pc:
                    continue
                
                if dfs(nr, nc, r, c, color):
                    return True
        
        return False

    for i in range(n):
        for j in range(m):
            if not visited[i][j]:
                if dfs(i, j, -1, -1, board[i][j]):
                    return "Yes"
    
    return "No"


if __name__ == "__main__":
    n, m = map(int, input().split())
    board = [list(input().strip()) for _ in range(n)]
    print(solve(n, m, board))
