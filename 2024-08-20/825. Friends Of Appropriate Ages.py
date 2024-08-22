from typing import List

# 825. Friends Of Appropriate Ages

# n persons on site, input array ages, where it's the age of each person

# ages = [16,16]
# 2

# each person sends another person friend request
# x should not send request to self
# if any of the below condition is true, no friend requests sent:

# x would not send a request to  y
# age[y] <= 0.5 * age[x] + 7
# age[y] > age[x]
# age[y] > 100 && age[x] < 100

# note: if x sends to y, y may not necessarily send request to x

# Example 1:

# Input: ages = [16,16]
# Output: 2
# Explanation: 2 people friend request each other.
# Example 2:

# Input: ages = [16,17,18]
# Output: 2
# Explanation: Friend requests are made 17 -> 16, 18 -> 17.
# Example 3:

# Input: ages = [20,30,100,110,120]
# Output: 3
# Explanation: Friend requests are made 110 -> 100, 120 -> 110, 120 -> 100.

# Constraints:

# n == ages.length
# 1 <= n <= 2 * 10^4
# 1 <= ages[i] <= 120

# goal => return total number of friend requests

class Solution:
  	def countFriendRequests(self, ages: List[int]) -> int:
		# we check each person against each other person to see if they satisfy the constraint
		# if isValid, we increment count, finally return count

		# approach 2:
		# sort the friends list in ascending order
		# find the pivot point where the first 2 constraints can be satisfied (age: 14)
		# break the input at the 100 age mark
		# use 2 pointers to mark the bounds where friend requests can be made
			# right pointer HAS to be to the right of left
			# for each value at the right pointer, calculate the left pointer with the formula (0.5 * nums[r] + 7)
			# move left pointer to be <= the calculation

# time => (NlogN)
# space => (1)


# x = 99, y = 55


	# x would not send a request to  y
	# age[y] <= 0.5 * age[x] + 7  # age[y] > 0.5 * age[x] + 7    x= 2  y >8   # send request x > 14 : it is possible x -> y
	# age[y] > age[x]   																											# send request age[y] <= age[x]  y <= 2   
	# age[y] > 100 && age[x] < 100 -> x < 100 < y -> x < y  									# send request y <= x  y == 98 x = 99
	def willSend(self, x: int, y: int) -> bool:
		# return y > 0.5 * x + 7 or y <= x or (y < 100 and x > 100)
		# y <= x 
		# y < 0.5 * x + 7
          
class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        cnt = [0] * 121
        for age in ages:
            cnt[age] += 1
        pre = [0] * 121
        for i in range(1, 121):
            pre[i] = pre[i - 1] + cnt[i]  #pre[i] count person number whose age <= age of pre[i]
        
        ans = 0
        for i in range(15, 121): # do not count < 14
            if cnt[i] > 0:
                bound = int(i * 0.5 + 7)
                ans += cnt[i] * (pre[i] - pre[bound] - 1)
        return ans
 #time complexity O(n + c) c=120
 #space complexity O(c)


 class Solution:
    def numFriendRequests(self, ages):
        ages.sort()
        n = len(ages)
        ans = 0
        i = 0
        j = 0

        for k in range(n):
            while i < k and not self.check(ages[i], ages[k]):
                i += 1 # i would not send k
            if j < k:
                j = k
            while j < n and self.check(ages[j], ages[k]):
                j += 1 # j > k  j would send to k
            if j > i:
                #    10 14 17 24 27  k= 34  37   48 59 60
                #       i                            j
                ans += j - i - 1

        return ans

    def check(self, x, y): 	#would send
        if y <= 0.5 * x + 7:
            return False #False = not send
        if y > x:
            return False
        if y > 100 and x < 100:
            return False
        return True
