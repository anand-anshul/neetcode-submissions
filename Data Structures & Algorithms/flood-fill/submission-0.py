class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        origin_color = image[sr][sc]
        if origin_color == color:
            return image
            
        image[sr][sc] = color
        q = deque([(sr, sc)])

        dirn = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while q:
            for i in range(len(q)):
                r, c = q.popleft()

                for d in dirn:
                    nr, nc = r + d[0], c + d[1]
                    if (
                        0 <= nr < len(image) and 
                        0 <= nc < len(image[0]) and 
                        image[nr][nc] == origin_color
                    ):
                        image[nr][nc] = color
                        q.append((nr, nc))
        
        return image