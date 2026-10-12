class TrieNode:
    def __init__(self, val = ""):
        self.val = val
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
        cur_children = self.root.children
        cur_node = self.root
        for c in word:
            if c in cur_children:
                cur_node = cur_children[c]
                cur_children = cur_children[c].children
            else:
                cur_children[c] = TrieNode()
                cur_node = cur_children[c]
                cur_children = cur_children[c].children
            
        cur_node.end_word = True

        


    def search(self, word: str) -> bool:
        cur_children = self.root.children
        cur_node = self.root
        for c in word:
            if c in cur_children:
                cur_node = cur_children[c]
                cur_children = cur_children[c].children
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
        
        