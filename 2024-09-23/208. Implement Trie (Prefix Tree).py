from typing import List
# 208. Implement Trie (Prefix Tree)
# A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

# Implement the Trie class:

# Trie() Initializes the trie object.
# void insert(String word) Inserts the string word into the trie.
# boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
# boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.
 

# Example 1:

# Input
# ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
# [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
# Output
# [null, null, true, false, true, null, true]

# Explanation
# Trie trie = new Trie();
# trie.insert("apple");
# trie.search("apple");   // return True
# trie.search("app");     // return False
# trie.startsWith("app"); // return True
# trie.insert("app");
# trie.search("app");     // return True
 

# Constraints:

# 1 <= word.length, prefix.length <= 2000
# word and prefix consist only of lowercase English letters.
# At most 3 * 10^4 calls in total will be made to insert, search, and startsWith.

class Node:
    def __init__(self, char: str) -> None:
        self.char = char
        self.children = {}
        self.isEnd = False


class Trie:
    def __init__(self) -> None:
        self.head = Node()

    def insert(self, word: str) -> None:
        # iterate through the characters, if character exists in Node's children, move down the tree
        # if char does not exist in children, create new Node and attach
        # mark the last character's node's isEnd flag to True
        node = self.head
        for ch in word:
            if ch in node.children:
                node = node.children[ch]
            else:
                node.children[ch] = Node(ch)
                node = node.children[ch]
        node.isEnd = True


    def search(self, word: str) -> bool:
        # use self.startsWith to perform the search
        node = self.head
        for ch in word:
            if ch in node.children and not node.isEnd:
                node = node.children[ch]
            else:
                return False
        
        
        return node.isEnd


    def startsWith(self, word: str) -> bool:
        # iterate through the characters, check each one against the children of the Trie
        # "app"
        node = self.head
        for ch in word:
            if ch in node.children:
                node = node.children[ch]
            else:
                return False
        
        return True

# time =>
# insert => O(n) where n is the length of the string
# search => O(n)
# startsWith => (n)

# space =>
# insert => O(26) where n is the length of the string
# search => O(1)
# startsWith => (1)