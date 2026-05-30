class TrieNode():
    def __init__(self) -> None:
        self.children = {}
        self.word = False

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        res = set()
        visited = set()
        def insert(word):
            cur = root
            for c in word:
                if c not in cur.children:
                    cur.children[c] = TrieNode()
                #print(cur.children)
                cur = cur.children[c]
                
            cur.word = True
        # def search(word, cur = root):
        #     ### FIRST VALUE IS IF WE FIND A PREFIX, SECOND VALUE IS IF WORD EXISTS
        #     # print(cur.children)
        #     for c in word:
        #         if c not in cur.children:
        #             return (False, False)
        #         cur = cur.children[c]
        #     return (True, cur.word)
        
        # def startsWith(prefix):
        #     cur = root
        #     for c in prefix:
        #         if c not in cur.children:
        #             return False
        #         cur = cur.children[c]
        #     return True
        
        def dfs(r,c, cur, current_word):

            directions = [[1,0], [-1, 0], [0, -1], [0, 1]]

            # print(r,c,current_word)
            # print(visited)

            if (r,c) not in visited and 0 <= r < len(board) and 0 <= c < len(board[0]):
                current_word += board[r][c]
                # search_res = search(board[r][c], cur)
                if not board[r][c] in cur.children:
                    #print("RETURNING FALSE")
                    return False
                cur = cur.children[board[r][c]]
                #print(cur.children)
                visited.add((r,c))
                
                if current_word not in res and cur.word:
                    #print("FOUND WORD", current_word)
                    res.add(current_word)
                for dr, dc in directions:
                    new_r = r + dr
                    new_c = c + dc
                    dfs(new_r, new_c, cur, current_word)
                visited.remove((r,c))
                
        for word in words:
            #print("INSERTING", word)
            insert(word)
        
        for i in range(len(board)):
            for j in range (len(board[0])):
                dfs(i, j, root, "")
                visited = set()
        
        return list(res)
        

        