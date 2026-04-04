class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        res = 0
        wordList = set(wordList)

        q = deque()
        q.append(beginWord)

        while q:
            res += 1
            length = len(q)
            for _ in range(length):
                curr = q.popleft()
                if curr == endWord:
                    return res
                for c in range(len(curr)):
                    for i in range(ord('a'),ord('z')+1):
                        new_word = curr[:c] + chr(i) + curr[c+1:]
                        if new_word in wordList:
                            wordList.remove(new_word)
                            q.append(new_word)
        return 0
                

