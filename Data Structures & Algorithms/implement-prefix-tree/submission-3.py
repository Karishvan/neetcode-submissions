class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_word = False

class PrefixTree:

    def __init__(self):
        """
                d
            o   e      r
        g       s           o
        """
        self.root = TrieNode()


    def insert(self, word: str) -> None:
        cur_node = self.root
        for c in word:
            if c not in cur_node.children:
                cur_node.children[c] = TrieNode()
            cur_node = cur_node.children[c]
            
        cur_node.end_word = True

        


    def search(self, word: str) -> bool:
        cur_node = self.root
        for c in word:
            if c in cur_node.children:
                cur_node = cur_node.children[c]
            else:
                return False

        return cur_node.end_word
        

    def startsWith(self, prefix: str) -> bool:
        cur_children = self.root.children

        for c in prefix:
            if c in cur_children:
                cur_children = cur_children[c].children
            else:
                return False
        
        return True
        
        