class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList_set = set(wordList)
        if endWord not in wordList_set:
            return 0

        def bfs():
            q = deque()
            q.append(beginWord)
            
            current_distance = 1
            visited = set()
            visited.add(beginWord)
            while q:
                for i in range(len(q)):
                    viable_word = q.popleft()
                    if viable_word == endWord:
                        return current_distance
                    for pos in range(len(viable_word)):
                        for c_offset in range(26):
                            new_char = chr((ord(viable_word[pos]) - 97 + c_offset) % 26 + 97)
                            new_word = viable_word[:pos] + new_char + viable_word[pos+1:]
                            if new_word not in visited and new_word in wordList_set:
                                q.append(new_word)
                                visited.add(new_word)
                current_distance += 1
            return 0
        
        return bfs()

            
                            