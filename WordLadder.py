import collections
class Solution(object):
    def __init__(self):
        self.wordGraph = collections.defaultdict(list)
    
    def ladderLength(self, beginWord, endWord, wordList):
        self.create_graph(wordList + [beginWord] + [endWord])
        return self.shortestPathBFS(beginWord, endWord)
    
    def create_graph(self, wordList):
        for word1 in wordList:
            for word2 in wordList:
                if self.adjancent_word(word1, word2):
                    self.wordGraph[word1] += [word2]
        
        print self.wordGraph

    def adjancent_word(self, word1, word2):
        diff = 0
        for char_combination in zip(word1, word2):
            if char_combination[0] != char_combination[1]:
                diff += 1
        
        return diff == 1
    
    def shortestPathBFS(self, startWord, endWord, visited=set()):
        queue = [(startWord, 1)]
        
        while queue:
            word, count = queue.pop(0)
            if word == endWord:
                return count
            if word in visited:
                continue

            for adjancent_word in self.wordGraph[word]:
                queue.append([adjancent_word,count + 1])
            
            visited.add(word)
