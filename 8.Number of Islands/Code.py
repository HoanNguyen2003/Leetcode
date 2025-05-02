class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        # count = 0
        # island = "1"
        # lookup = []
        # for i in range(len(grid)):
        #     for j in range(len(grid[0])):
        #         if grid[i][j] == "1":
        #             if([i+1,j] in lookup or [i,j+1] in lookup or [i-1,j] in lookup or [i,j-1] in lookup):
        #                 lookup.append([i,j])
        #             else:
        #                 count += 1
        #                 lookup.append([i,j]) 

        # return count

        rows, cols = len(grid), len(grid[0])
        count = 0

        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] != "1":
                return
                
            grid[r][c] = "0"
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    dfs(i, j)
                    count += 1

        return count

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
run = Solution()
print(run.numIslands(grid))

# Output: 3