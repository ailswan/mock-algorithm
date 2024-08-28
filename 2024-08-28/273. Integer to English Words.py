from typing import List
# 273. Integer to English Words
#  Convert a non-negative integer num to its English words representation.

 

# Example 1:

# Input: num = 123
# Output: "One Hundred Twenty Three"
# Example 2:

# Input: num = 12345
# Output: "Twelve Thousand Three Hundred Forty Five"
# Example 3:

# Input: num = 1234567
# Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
 

# Constraints:

# 0 <= num <= 2^31 - 1

class Solution:
	def numToEnglish(self, num: int) -> str:
		# split number into digits, break into groups (ie: 0's -> hundreds, thousands, millions, billions, trillions) groups of 3
		# the last number is always just the number in English (one -> nine)
		# tens -> ten, twenty, thirty, forty, fifty, sixty, seventy, eighty, ninety
		# hundreds -> combine the "ones" and "tens"
		ans = ""
		ones=["One","Two","Three","Four","Five","Six","Seven","Eight","Nine"]
		Tens_1=["Ten","Eleven","Twelve",'Thirteen','Fourteen','Fifteen','Sixteen','Seventeen',"Eighteen","Nineteen"]
		Tens_2=['Twenty','Thirty','Forty','Fifty','Sixty','Seventy','Eighty','Ninety']
		unit=["","Thousand","Million",'Billion']

		digits = [] # [5, 6, 7]  [456, 231, 234, 567]
		while num:
			digits.append(num % 1000)
			num = num // 1000

    # 456231234567
		#digits = [567, 234, 456, 231,]
		#           0    1   2    3
		#           " "  "T" "M"  "B"  unit
		# group = 0
		n = len(digits)
		
		for number in enumerate(digits):# ans = 567 number = 234   unit[i]=Thousand   
			group = self.helper(number) + " " + unit[i]    
			ans = group + ans                         # 234 Thousand 567 
		return ans.strip()


		#  567
        #  [456,    231,     234,   567]   len= 7  6
		#    billion  million  thousand
		# reverse the digits and process it by groups of 3
		# helper(n) n = 567 -> english
			
		# Input: num = 1234567
		# len(digits) = 6
		# for i in range(n - 1, -1, 3): range(4)
		# 	ans += self.helper(int("".join(digits[i + 2:i]), group)) 
		# 	group += 1
		# 	if ptr > 0:
		# 		ans += self.helper(int("".join(digits[:ptr])), group)

		# return ans
#   6000 000 
		def helper(self, num): #567  5 15      67 20-10  7  0
			ans = ""
			if num == 0:
				return ""
			if num >= 100:
				# ones_digit = num % 10
				# num = num // 10
				hundreds_digit = num % 100 # 67
				num = num // 100  # "Five Hundred"
				ans += ones[hundreds_digit - 1] + " " + "Hundred"
			if num >= 10 and num < 20: #0- 10 1 - 11  2- 12  5- 15
				idx = num % 10
				ans += " " + Tens_1[idx]
				return ans
			if num < 100 and num >= 20:
				tens_digit = num % 10
				num = num // 10
				ans += " " + Tens_2[tens_digit - 2] #   0 - 20 1- 30
			if num < 10:
				ans = ans + " " + ones[num - 1]

			return ans