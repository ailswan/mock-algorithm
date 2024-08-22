from typing import List

'''
input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
output: true
'''
import collections
class Solution:
    def isValid(self, words: List[str], order: str) -> bool:
        #words = ["hello","leetcode"] order = "hlabcdefgi j k m n o p q  r s t u v w x y z"
        #          0       1                   012345678910 111213141516 17181920 2122232425
        #loop word(w) in words: 
        # while compare indexes of letters in curr and pre
        dic = collections.defaultdict(int)
        for i in range(len(order)):
            dic[order[i]] = i
        if len(words) <= 1:
            return True
        for i in range(1, len(words)):#  "hello","leetcode"
            p, w = words[i - 1], words[i]# "hello","leetcode" 5  8 
            min_l = min(len(p), len(w)) # 5
            j = 0
            while j < min_l:# 0< 5
                if dic[p[j]] > dic[w[j]]:# h   l   0 1 
                    return False
                elif dic[p[j]] < dic[w[j]]:
                    break
                else:
                    j += 1
            if len(w) <= len(p):# helloh  hello
                return False
        return True
        #time complexity O(n) n = length of words O(n * m) m=  length of the longest word
        #space complexity O(1) 
            
                  
            


      
    
 



