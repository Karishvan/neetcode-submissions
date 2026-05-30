class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        directions = [[1,0], [0,1], [-1,0], [0, -1]]
        #return False
        def dfs(character_index, r, c):
            # print(visited)
            res = False
            if character_index == len(word):
                return True
            if (r,c) not in visited and r in range (len(board)) and c in range (len(board[0])) and board[r][c] == word[character_index]:
                character_index += 1
                visited.add((r, c))
                print("FOUND LETTER", board[r][c], " AT INDEX ", r, c)
                
                for (dx, dy) in directions:
                    res = res or dfs(character_index, r+dx, c+dy)
                
                visited.remove((r, c))
                return res
            else:
                return False
            # if not res:
            #     visited.clear()
            
            
        
        
        letter_index = 0
        for i in range (len(board)):
            for j in range (len(board[0])):
                if dfs(0, i, j): return True
                

        return False

        
