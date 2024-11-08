from typing import List
# 676. Implement Magic Dictionary

# Design a data structure that is initialized with a list of different words. Provided a string, 
# you should determine if you can change exactly one character in this string to match any word in the data structure.

# Implement the MagicDictionary class:

# MagicDictionary() Initializes the object.
# void buildDict(String[] dictionary) Sets the data structure with an array of distinct strings dictionary.
# bool search(String searchWord) Returns true if you can change exactly one character in searchWord to match any string in the data structure, 
# otherwise returns false.
 

# Example 1:

# Input
# ["MagicDictionary", "buildDict", "search", "search", "search", "search"]
# [[], [["hello", "leetcode"]], ["hello"], ["hhllo"], ["hell"], ["leetcoded"]]
# Output
# [null, null, false, true, false, false]

# Explanation
# MagicDictionary magicDictionary = new MagicDictionary();
# magicDictionary.buildDict(["hello", "leetcode"]);
# magicDictionary.search("hello"); // return False
# magicDictionary.search("hhllo"); // We can change the second 'h' to 'e' to match "hello" so we return True
# magicDictionary.search("hell"); // return False
# magicDictionary.search("leetcoded"); // return False
 

# Constraints:

# 1 <= dictionary.length <= 100
# 1 <= dictionary[i].length <= 100
# dictionary[i] consists of only lower-case English letters.
# All the strings in dictionary are distinct.
# 1 <= searchWord.length <= 100
# searchWord consists of only lower-case English letters.
# buildDict will be called only once before search.
# At most 100 calls will be made to search.

class Node:
    def __init__(self, val = None, children = {}, isEnd = False) -> None:
        self.val = val
        self.children = children
        self.isEnd = isEnd

class Trie:
    def __init__(self) -> None:
        self.root = Node()

class MagicDictionary:
    # if input string is the same as a word in the dictionary, return False... cannot change a single char to match dictionary word
    # if length is not the same as word in dictionary, return False

    # we should keep the length of each word in the dictionary
    # we can build a trie to store all the words in the dictionary
    # iterate through input string and perform BFS/DFS scan through trie

    def __init__(self):
        self.trie = Trie()

    def buildDict(self, dictionary: List[str]) -> None:
        # iterate through the words and populate trie
        for word in dictionary:
            root = self.trie.root
            for ch in word:
                if ch in root.children:
                    root = root.children[ch]
                else:
                    root.children[ch] = Node(ch)
                    root = root.children[ch]
            root.isEnd = True

    def search(self, searchWord: str) -> bool:
        changes = 0
        ans = False
        root = self.trie.root
        for i, ch in enumerate(searchWord):
            if ch in root.children:
                root = root.children[ch]
            else:
                changes += 1
                if changes > 1:
                    return False
                ans = self.dfs(searchWord[i + 1:], root)
        return ans

    def dfs(self, word, root) -> bool:
        for ch in word:
            if ch in root.children:
                root = root.children[ch]
            else:
                return False
        return root.isEnd
    
# time =>
# buildDict -> O(N * M) where N is the number of words in dictionary and M is the average length of each word
# search -> O(M) where M is the length of the word

# space =>
# buildDict -> O(26 * M) the entire alphabet, 26 letters... and M is the average length of the word
# search -> O(1)


class MagicDictionary:

    def __init__(self):
        self.words = list()


    def buildDict(self, dictionary: List[str]) -> None:
        self.words = dictionary

    def search(self, searchWord: str) -> bool:
        for word in self.words:
            if len(word) != len(searchWord):
                continue
            
            diff = 0
            for x, y in zip(word, searchWord):
                if x != y:
                    diff += 1
                    if diff > 1:
                        break
            if diff == 1:
                return True
            
        return False
