from typing import List

# 211. Design Add and Search Words Data Structure

# Design a data structure that supports adding new words and finding if a string matches any previously added string.

# Implement the WordDictionary class:

# WordDictionary() Initializes the object.
# void addWord(word) Adds word to the data structure, it can be matched later.
# bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.
 

# Example:

# Input
# ["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
# [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
# Output
# [null,null,null,null,false,true,true,true]

# Explanation
# WordDictionary wordDictionary = new WordDictionary();
# wordDictionary.addWord("bad");
# wordDictionary.addWord("dad");
# wordDictionary.addWord("mad");
# wordDictionary.search("pad"); // return False
# wordDictionary.search("bad"); // return True
# wordDictionary.search(".ad"); // return True
# wordDictionary.search("b.."); // return True
 

# Constraints:

# 1 <= word.length <= 25
# word in addWord consists of lowercase English letters.
# word in search consist of '.' or lowercase English letters.
# There will be at most 2 dots in word for search queries.
# At most 104 calls will be made to addWord and search.

class Node:
    def __init__(self, ch = None) -> None:
        self.char = ch
        self.children = {}
        self.isEnd = False


class WordDictionary:

    # Input
    # ["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
    # [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
    def __init__(self):
        # trie data structure
        # when we add words, add the characters to the trie if it doesn't exist
        # for searching, make sure all characters match... for any '.' in the search string, iterate through all children of a node in the Trie
        self.head = Node()

    def addWord(self, word: str) -> None:
        root = self.head

        for char in word:
            if char in root.children:                                       # (b)                   (d)             (m)             (p)
                root = root.children[char]                                 # /   \                  /   \           /   \          /    \
            else:                                                         # (a)                    (a)             (a)           (a)
                new_node = Node(char)                                     # /                       /              /            /
                root.children[char] = new_node                           # (d)                     (d)            (d)          (d)
                root = root.children[char]
        root.isEnd = True

    def search(self, word: str) -> bool:
        root = self.head
        isValid = True

        for i, ch in enumerate(word):
            if ch == '.':
                # iterate through all the children of the node
                for chrs in root.children:
                    isValid = self.search(chrs + word[i + 1:])
                    if isValid:
                        return True
                if isValid == False:
                    return False
            else:
                if ch in root.children:
                    root = root.children[ch]
                else:
                    return False
        
        return root.isEnd


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

# time => add: O(k) where k is the length of the word
# space => add: O(n * k) where n is the total number of words that are stored

# time => search: O(n*26^d) where n is the length of the word and m is the node with the most children
# -Best case: O(n) when there are no . wildcards and the search string is fully matched character by character.
# -Worst case: 𝑂(26^𝑑⋅𝑛)when there are 𝑑 wildcards in the search string, and  n is the length of the search string.
# space => search: O(1)

# The space complexity for storing the Trie depends on the total number of nodes.
# In the worst case, where all the characters are unique and the Trie has to store each character individually, the space complexity is O(n⋅k), where n is the number of words and k is the average length of the words.
# Space complexity: O(n⋅k).