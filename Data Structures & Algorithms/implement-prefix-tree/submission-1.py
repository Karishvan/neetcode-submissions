class TreeNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False

class PrefixTree:

    def __init__(self):
        self.trie = TreeNode()

    def insert(self, word: str) -> None:
        trie_node = self.trie
        for c in word:
            if c not in trie_node.children:
                trie_node.children[c] = TreeNode()
                #print(trie_node.children[c])    
            trie_node = trie_node.children[c]
            # print(child.val)
            # print(child.children)
            # print(trie_node.children[)
        trie_node.end_of_word = True
        #print("INSERT")
        #print(self.trie.children)


    def search(self, word: str) -> bool:
        #rint("SEARCHING")
        child = self.trie
        for c in word:
            # print(c)
            # print(child.children)
            if c not in child.children:
                return False
            child = child.children[c]
        # print(child.children)
        return child.end_of_word


    def startsWith(self, prefix: str) -> bool:
        #print("STARTS WITH")
        child = self.trie
        for c in prefix:
            if c not in child.children:
                return False
            child = child.children[c]
        return True
        