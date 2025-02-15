class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        if not mat:
            return mat


        # Making infinity value matrix
        rows, cols = len(mat), len(mat[0])
        dist = [[float('inf') for _ in range(cols)] for _ in range(rows)]
        queue = deque()

        # Putting zero in the infinity matrix
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    dist[i][j] = 0
                    # adding zero to a queue
                    queue.append((i,j))
        
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        # Dequeuing the zero from infinity matrix
        while queue:
            x, y = queue.popleft()
            for dx, dy in directions:
                # from 4 directions picking one by one and checking direction is possible or not
                nx, ny = x+dx, y+dy
                if 0<=nx<rows and 0<=ny<cols:
                    # checking direction value is bigger than current distance from zero+1, would be infinity
                    if dist[nx][ny] > dist[x][y] + 1:
                        # if yes updating it with +1 and adding the new direction to the queue to check further directions
                        dist[nx][ny] = dist[x][y] + 1
                        queue.append((nx,ny))
        
        return dist
                
        