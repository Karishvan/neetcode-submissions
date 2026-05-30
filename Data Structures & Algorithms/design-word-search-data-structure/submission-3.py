class TrieNode():
    def __init__(self) -> None:
        self.children = {}
        self.end_of_word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.end_of_word = True
        
        

    def search(self, word: str) -> bool:
        cur = self.root
        #print(word)
        def dfs(i, cur):
            if i == len(word) and cur.end_of_word:
                return True
            elif i == len(word):
                #print(i)
                return False
            if word[i] != "." and word[i] not in cur.children:
                return False
            if word[i] == ".":
                res = False
                for k,v in cur.children.items():
                    res = res or dfs(i+1, v)
                return res
            else:
                v = cur.children[word[i]]
                return dfs(i+1, v)
        res = dfs(0, cur)
        return res


                
