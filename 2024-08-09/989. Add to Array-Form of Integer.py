from typing import List

# 989. Add to Array-Form of Integer

# The array-form of an integer num is an array representing its digits in left to right order.

# For example, for num = 1321, the array form is [1,3,2,1].
# Given num, the array-form of an integer, and an integer k, return the array-form of the integer num + k.

 

# Example 1:

# Input: num = [1,2,0,0], k = 34
# Output: [1,2,3,4]
# Explanation: 1200 + 34 = 1234
# Example 2:

# Input: num = [2,7,4], k = 181
# Output: [4,5,5]
# Explanation: 274 + 181 = 455
# Example 3:

# Input: num = [2,1,5], k = 806         some carry is needed
# Output: [1,0,2,1]
# Explanation: 215 + 806 = 1021
 

# Constraints:

# 1 <= num.length <= 104
# 0 <= num[i] <= 9
# num does not contain any leading zeros except for the zero itself.
# 1 <= k <= 104

class Solution:
    def find_sum(self, num_arr: List[int], k: int) -> List[int]:     # num_arr[-1] += k    [2,1,811]  carry = 81  1 [2,82,1] carry = 8 [10,2,1]  [1] +[0,2,1] = [1,0,2,1]
        # perform addition
        # set up a c for carry
        # transform k into a list
        # add digits from right to left
        c = 0
        arr_k = list(map(int, str(k)))# int 345   [3, 4, 5] list(map(int, str(k)))
        n = min(len(num_arr), len(arr_k))               # 2       
        ans = [0] * max(len(num_arr), len(arr_k))       # [0, 0, 0, 0]
        # left pad the smaller length number with 0's so that they are the same length
                                                                                            #[1,1,1,1,1,1]
                                                                                            #[0,1,2,3,4,5]  i == 2    n - i == length of backward part
        if len(num_arr) < len(arr_k):
            num_arr = [0] * len(arr_k) - len(num_arr) + num_arr                         # num_arr = [1, 2, 3, 4]
        elif len(num_arr) > len(arr_k):                                                 # arr_k =   [3, 5]                         ---> [0, 0, 3, 5]
            arr_k = [0] * len(num_arr) - len(arr_k) + arr_k

        for i in range(len(num_arr) - 1, -1, -1):                # 1   range(maxlen - 1, -1, -1)    3 #arr_val = arr_k[i] if maxLen - i <= len(arr) else 0
            curr_sum = arr_k[i] + num_arr[i] + c      # 4 + 0 + 0 => 4                                #  num_val = num_arr[i] if maxLen - i <= len(num) else 0
            if curr_sum > 9:                #curr_sum 12
                c += 1
                digit = curr_sum % 10
                ans[n + i - 1] = digit    #      9,9,9,10,1,12
            else:
                ans[n + i - 1] = curr_sum                       # [0, 0, 0, 4]
            c = 0
        
        # TODO: whichever number has more digits need to be added to ans
        j = 0
        while j < len(ans) - n:
            ans[j] = ans[n - 1 - j] + c
            c = 0

        return ans

# Input: num = [1,2,0,0], k = 34