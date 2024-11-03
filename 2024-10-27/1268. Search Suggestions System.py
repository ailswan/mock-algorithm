from typing import List

# 1268. Search Suggestions System

# You are given an array of strings products and a string searchWord.

# Design a system that suggests at most three product names from products after each character of searchWord is typed. Suggested products should have common prefix with searchWord. If there are more than three products with a common prefix return the three lexicographically minimums products.

# Return a list of lists of the suggested products after each character of searchWord is typed.

 

# Example 1:

# Input: products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
# Output: [["mobile","moneypot","monitor"],["mobile","moneypot","monitor"],["mouse","mousepad"],["mouse","mousepad"],["mouse","mousepad"]]
# Explanation: products sorted lexicographically = ["mobile","moneypot","monitor","mouse","mousepad"].
# After typing m and mo all products match and we show user ["mobile","moneypot","monitor"].
# After typing mou, mous and mouse the system suggests ["mouse","mousepad"].
# Example 2:

# Input: products = ["havana"], searchWord = "havana"
# Output: [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]
# Explanation: The only word "havana" will be always suggested while typing the search word.
 

# Constraints:

# 1 <= products.length <= 1000
# 1 <= products[i].length <= 3000
# 1 <= sum(products[i].length) <= 2 * 104
# All the strings of products are unique.
# products[i] consists of lowercase English letters.
# 1 <= searchWord.length <= 1000
# searchWord consists of lowercase English letters.

class Trie:
    def __init__(self) -> None:
        self.child = {} #{a: }
        self.words = [] # [aa, ab ,ac]

    def insert(self, word):
        cur = self.root
        for i in range(len(word)):
            c = word[i]
            # if i == len(word) - 1:
            #         cur[c] = {cur[c],{"#": word}}
            if c not in cur:
                cur.child[c] = Trie()
            cur = cur.child[c]
            cur.words.append(word)
            cur.words.sort()
            if len(cur.words) > 3:
                cur.words.pop()

    def search(self, word): #m    m  {m: {a:{"#":["","",""], a:{c}, b, c},b:{} }} m - a   b   c  for a b c
        #     m
        #  a      b
        # # a b    {#:mb} c d
        #   #:{maa}
        # m[ma, maa, mab]
        cur = self.dic
        res = []
        for i in range(len(word)):
            c = word[i]
            if "#" in cur:
                res.append(cur)
            if c not in cur:
                return res
            cur = cur[c]
 
 

    # def find_word_by_prefix(self, prefix):
    #     node = self.root
    #     for c in prefix:
    #         if c not in node.children: return ''
    #         node = node.children[c] 
    #     return node.words

        
class SuggestionSystem:
    def __init__(self) -> None:
        self.p_t = Trie()
    def search(self, products: List[str], searchWord: str) -> List[List[str]]:
        # ["mobile","moneypot","monitor","mouse","mousepad"]  "mouse"
        # {pre: prds} prds[:3]
        # trie   {m}
        #      {o}
        #       {b n u}
        for prod in products:
            self.p_t.insert(prod)
        res = []
        cur = ''
        for c in searchWord:
            suggestion = self.p_t.search(cur + c)
            res.append(suggestion)
        return res



class Trie:
    def __init__(self):
        self.dic = {}

    def insert(self, word: str) -> None:
        cur = self.dic
        for c in word:
            if c not in cur:
                cur[c] = {}
            cur = cur[c]
        cur['#'] = True

    def search(self, word: str) -> bool:
        cur = self.dic
        for c in word:
            if c not in cur:
                return False
            cur = cur[c]
        return '#' in cur

    def startsWith(self, prefix: str) -> bool:
        cur = self.dic
        for c in prefix:
            if c not in cur:
                return False
            cur = cur[c]
        return True



class TrieNode:
    def __init__(self):
        self.children = dict()
        self.words = list()
        self.n = 0
        # self.char = char
        # self.children = {}
        # self.isEnd = False
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def add_word(self, word):
        node = self.root
        for c in word:
            if c not in node.children: node.children[c] = TrieNode()
            node = node.children[c] 
            if node.n < 3:
                node.words.append(word)
                node.n += 1
        
    def find_word_by_prefix(self, prefix):
        node = self.root
        for c in prefix:
            if c not in node.children: return ''
            node = node.children[c] 
        return node.words
            
class Solution:
    def suggestedProducts(self, A: List[str], searchWord: str) -> List[List[str]]:
        A.sort()
        trie = Trie()
        for word in A: trie.add_word(word)
        ans, cur = [], ''
        for c in searchWord:
            cur += c 
            ans.append(trie.find_word_by_prefix(cur))
        return ans    