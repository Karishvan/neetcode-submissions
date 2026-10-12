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
                    viable_word_char_array = list(viable_word)
                    for pos in range(len(viable_word)):
                        original_letter = viable_word[pos]
                        for c_offset in range(26):
                            new_char = chr(c_offset + ord('a'))
                            if new_char == original_letter:
                                continue
                            viable_word_char_array[pos] = new_char
                            new_word = "".join(viable_word_char_array)
                            if new_word not in visited and new_word in wordList_set:
                                q.append(new_word)
                                visited.add(new_word)
                            viable_word_char_array[pos] = original_letter
                current_distance += 1
            return 0
        
        return bfs()

            
                            