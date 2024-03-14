"""
[["A","B","C","E"],
 ["S","F","C","S"]
 ["A","D","E","E"]], word = "ABCCED"
-> true
- dfs로 문자열을 찾을수 있는지 탐색

4방향으로 dfs 보내고 path에서 (x, y) remove 해줘야함
"""

from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(x, y, i):

            # return condition
            if x<0 or x>=n or y<0 or y>=m or \
                (x, y) in path or board[x][y] != word[i]: 
                return False
            
            if i == len(word)-1 and board[x][y] == word[i]: return True

            path.add((x, y))
            # next search
            res = dfs(x+1, y, i+1) or dfs(x-1, y, i+1) or dfs(x, y+1, i+1) or dfs(x, y-1, i+1)
            path.remove((x, y))
            return res
        
        
        # initialize necessary data structure
        n, m = len(board), len(board[0])
        path = set([])

        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]: 
                    # print(f"start search, {board[i][j], word[0], i, j}")
                    if dfs(i, j, 0): return True
        
        return False

# ans = Solution().exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED")
# ans = Solution().exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE")
# ans = Solution().exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB")
ans = Solution().exist([["A","B","C","E"],
                        ["S","F","E","S"],
                        ["A","D","E","E"]], "ABCESEEEFS")

print(ans)
            