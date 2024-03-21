from typing import List, Type, TypeVar

class Trie:
    def __init__(self) -> None:
        self.children = {}      # 자식 노드
        self.isWord = False     # is it leaf node?
        
    def addWord(self, word: str):
        cur = self              # 현재 자기 자신으롤 current pointer 초기화
        for w in word:          # word 각 알파벳 돌면서 노드로 만들어서 children으로 달아주기
            if w not in cur.children: # 이미 추가되어있는 노드면 넘어가고, 아니면 다음 알파벳 추가
                cur.children[w] = Trie()
            cur = cur.children[w]
        cur.isWord = True       # word가 'apple' 들어왔으면 노드 다섯개 연결해서 만들어놓고 마지막 e에 대한 노드는 isword True로 설정해서 Leaf node라는 것 체크

TTrie = TypeVar("TTrie", bound = Trie)

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        """
        word 하나 기준으로 얘 찾을 수 있는지 없는지 dfs하는게 아니라,
        word 전체 Trie로 만들어 놓고, board 각 좌표에서 dfs시작해서 
            - out of range인지 확인
            - 이미 방문한 좌푠지 확인
            - 다음 위치로 탐색 이어갈 수 있는지 확인(다음 노드에 word 다음 알파벳 있는지 확인)
        해나가면서 isWord()
        """
        def dfs(r:int, c:int, w: str, cur_node: Type[TTrie]):

            """
            r, c : 현재 좌표 
            w : 현재까지 tracking 한 문자열 리스트
            cur_node : 현재 노드(다음 search 하려면 cur_node.children[board[r][c]]) 로 탐색
            """
            
            # base case
            if r<0 or c<0 or r>=n or c>=m or \
            (r, c) in visited or \
            board[r][c] not in cur_node.children:
                return 
            
            print(r, c, w, cur_node.children)
            
            visited.add((r, c))
            cur_node = cur_node.children[board[r][c]]
            w += board[r][c]
            if cur_node.isWord: ans.add(w)

            dfs(r+1, c, w, cur_node)
            dfs(r, c+1, w, cur_node)
            dfs(r-1, c, w, cur_node)
            dfs(r, c-1, w, cur_node)
            visited.discard((r, c))

        n, m = len(board), len(board[0])
        visited, ans = set(), set()
        
        root = Trie()
        for word in words:
            root.addWord(word)
        print(f"root : {root.children})")

        # visited, ans = set(), set()
        for i in range(n):
            for j in range(m):
                    dfs(i, j, "", root)

        print(f"ans : {ans}")
        return list(ans)


    def findWords_mysolution(self, board: List[List[str]], words: List[str]) -> List[str]:
        n, m = len(board), len(board[0])
        start_point = {s:[] for s in list(set([word[0] for word in words]))}
        result = []

        for i in range(n): 
            for j in range(m):
                if board[i][j] in start_point.keys():
                    start_point[board[i][j]].append((i, j))
        
        def dfs2(x, y, target):
            # 탐색 실패한 후 다음 후보지 노드로 돌아갈 때 visited 초기화해줘야함
            # checkpoint처럼 4방향 탐색 시 stack에 두개 이상의 원소가 추가되면,
            # 즉 다음 s가 board의 두 방향 이상에 존재할 경우
            # 해당 s 위치를 checkpoint에 append 해두고 이후 경로 탐색에 실패하여 다음 후보지 시 visited rewind 작업에 사용한다.
            # checkpoint top 인덱스
            # visited 를 스냅샷처럼 찍어놓을 수 있는 로직 필요
            # visited의 checkpoint 지점(인덱스, 길이 등) 을 저장하는 checkpoint 변수 두기
            stk = [(x, y, 0)]
            visited = []
            trace_i = 0
            while stk:
                sx, sy, si = stk.pop()
                print(sx, sy, "v=",visited)
                for _ in range(trace_i-si): 
                    print("rewind visited")
                    visited.pop()
                print(f"v={visited}")
                # if visited and board[sx][sy] == visited[-1][0]
                trace_i = si

                if si == len(target)-1:
                    if board[sx][sy] == target[si]:
                        result.append(target)
                        return True
                    return False
                
                for dx, dy in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                    nx, ny = sx+dx, sy+dy
                    if 0<=nx<n and 0<=ny<m and (nx, ny) not in visited and board[nx][ny] == target[si+1]:
                        stk.append((nx, ny, si+1))
                visited.append((sx, sy))

        for word in words:
            for sp in start_point[word[0]]:
                print(f"start searching for {word}")
                if dfs2(sp[0], sp[1], word): break
        print(result)
        return result
    

Solution().findWords(board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"])
# Solution().findWords(board = [["a","b"],["c","d"]], words = ["abcb"])
# Solution().findWords(board = [["a","a"]], words = ["aaa"]) #[]
# Solution().findWords(board=[["a","b","c","e"],["x","x","c","d"],["x","x","b","a"]], words=["abc","abcd"])
# Solution().findWords(board=[["a","b","c"],["a","e","d"],["a","f","g"]], words=["abcdefg","gfedcbaaa","eaabcdgfa","befa","dgc","ade"])
# Solution().findWords(board=[["a","b","c"],["a","e","d"],["a","f","g"]], words=["eaafgdcba","eaabcdgfa"])
# Solution().findWords(board=[["a","b","e"],["b","c","d"]], words=["abcdeb"])