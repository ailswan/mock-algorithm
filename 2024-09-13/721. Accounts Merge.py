from typing import List
# 721. Accounts Merge
# Given a list of accounts where each element accounts[i] is a list of strings, where the first element accounts[i][0] is a name, and the rest of the elements are emails representing emails of the account.

# Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some common email to both accounts.
# Note that even if two accounts have the same name, they may belong to different people as people could have the same name. 
# A person can have any number of accounts initially, but all of their accounts definitely have the same name.

# After merging the accounts, return the accounts in the following format:
# the first element of each account is the name, and the rest of the elements are emails in sorted order. The accounts themselves can be returned in any order.

 

# Example 1:

# Input: accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
# Output: [["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
# Explanation:
# The first and second John's are the same person as they have the common email "johnsmith@mail.com".
# The third John and Mary are different people as none of their email addresses are used by other accounts.
# We could return these lists in any order, for example the answer [['Mary', 'mary@mail.com'], ['John', 'johnnybravo@mail.com'], 
# ['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']] would still be accepted.
# Example 2:

# Input: accounts = [["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]]
# Output: [["Ethan","Ethan0@m.co","Ethan4@m.co","Ethan5@m.co"],["Gabe","Gabe0@m.co","Gabe1@m.co","Gabe3@m.co"],["Hanzo","Hanzo0@m.co","Hanzo1@m.co","Hanzo3@m.co"],["Kevin","Kevin0@m.co","Kevin3@m.co","Kevin5@m.co"],["Fern","Fern0@m.co","Fern1@m.co","Fern5@m.co"]]
 

# Constraints:

# 1 <= accounts.length <= 1000
# 2 <= accounts[i].length <= 10
# 1 <= accounts[i][j].length <= 30
# accounts[i][0] consists of English letters.
# accounts[i][j] (for j > 0) is a valid email.

class Solution:
    def merge(self, accounts: List[List[str]]) -> List[List[str]]:
        # brute force => iterate through accounts, store the name in a dictionary (along with the emails), for a name already in dictionary, check if emails match, if so, extend it
        # otherwise, the same name person is a different person
    

# class Node:
#     def __init__(self, val, parent) -> None:
#         self.val = val
#         self.parent = parent

class UF:
    def __init__(self,n) -> None:
         self.parent = list(range(n))

    def union(self, a, b):
        # while a < b:
        

    def find(self, c):
        if c in self.parent:
            c = self.find(c)
        if c not in self.parent:
            return c
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        
    def union(self, index1: int, index2: int):
        self.parent[self.find(index2)] = self.find(index1)
       

    def find(self, index:int) -> int:
        if self.parent[index] != index:
            self.parent[index] = self.find(self.parent[index])
        return self.parent[index]

import collections
# Input: accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        emailToIndex = dict()
        emailToName = dict()
        for account in accounts:
            name = account[0]
            for email in account[1:]:
                if email not in emailToIndex:
                    emailToIndex[email] = len(emailToIndex)
                    emailToName[email] = name

            
        
        uf = UnionFind(len(emailToIndex))           # uf => self.parent = [0, 1, 2, 3]
        uf = UnionFind(len(emailToIndex))
        for account in accounts:
            firstIndex = emailToIndex[account[1]]   # 1: johnsmith@mail.com
            for email in account[2:]:
                uf.union(firstIndex,emailToIndex[email])    # 2: john_newyork@mail.com

        indexToEmails = collections.defaultdict(list)
        for email, index in emailToIndex.items():
            index = uf.find(index)
            indexToEmails[index].append(email)

        ans = list()
        for emails in indexToEmails.values():
            ans.append([emailToName[emails[0]]]+ sorted(emails))
        return ans