from typing import List

#  43. Multiply Strings
# Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

# Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.


# Example 1:

# Input: num1 = "2", num2 = "3"
# Output: "6"
# Example 2:

# Input: num1 = "123", num2 = "456"
# Output: "56088"
 

# Constraints:

# 1 <= num1.length, num2.length <= 200
# num1 and num2 consist of digits only.
# Both num1 and num2 do not contain any leading zero, except the number 0 itself.

# carry
# need to keep track of the positions of each "row" of multiplied values
# convert the final answer back to a string


class Solution:
  def multiplyString(self, s1: str, s2: str) -> str:
    # iterate backwards from the string
    # use pointers i,j to keep track of which element we are looking at in the inputs
    # make sure to keep track of the carry
    # use a 2-D array to keep track of the digits to be added
    # pre-populate the matrix with 0's as palceholders
    # after adding, we convert number back to string and return
    c = 0
    n = len(s1)    # n = 3
    m = len(s2)    # m = 3
    matrix = []
    #   9999 < 10000        9999             9999    #9999  j
    #     9  < 10            90               900    # 999  i
    #len  5  < 100000        6                  7  
    # r1     [89991] no lagging zeros
      #r2                   [899910] 1 lagging zero
      #r3                                  [8999100] 2 lagging zero          


# Input: num1 = "123", num2 = "456"
# Output: "56088"




    for i in range(n - 1, -1, -1):   # i = 2
      r = [0] * (n - i - 1)                         # i = 2 - 1; r = [0] * (2 - 1 - 1) --> [0] * 0
      for j in range(m - 1, -1, -1):  # j = 0
        val = int(s1[j]) * int(s1[i]) + c       # val = 3 * 6 + 0 => 18 ....... val = 2 * 5 + 1 => 11   ....... val = 1 * 4 + 1 => 5
        r = [val % 10] + r                      # r = [8] + []          ....... r = [val % 11] + [8] -> [1, 8]      ....... r = [val % 11] + [8] -> [1, 8]
        if val > 9:
          c = val // 10                          # c = 1                ....... c = 1
      if c:
        r = [c] + r
      c = 0
      matrix.append(r)


      # [
      #    [1,2,3],
      #    [5,6,0],
      #  [8,5,0,0]
      # ]

    add_carry = 0
    total = []
    max_row = max(len(matrix[r]) for r in matrix)

    for c in range(max_row - 1, -1, -1):
      sub_total = add_carry
      for r in range(len(matrix)):
        sub_total += matrix[r][c]
      sub_total += add_carry
      add_carry = sub_total // 10
      total.append(sub_total % 10)
    
    if add_carry:
      total = [add_carry] + total
    return "".join(total)

# time complexity => (n * m)
# space => (n * m)
# [::-1]









class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        # Reverse both numbers.
        first_number = num1[::-1]
        second_number = num2[::-1]

        # For each digit in second_number, multipy the digit by first_number and then
        # store the multiplication result (reversed) in the results array.
        results = []
        for index, digit in enumerate(second_number):
            results.append(self.multiply_one_digit(digit, index, first_number))

        # Add all of the results together to get our final answer (in reverse order)
        answer = self.sum_results(results)

        # Reverse answer and join the digits to get the final answer.
        return "".join(str(digit) for digit in reversed(answer))

    def multiply_one_digit(
        self, digit2: str, num_zeros: int, first_number: List[str]
    ) -> List[int]:
        """Multiplies first_number by a digit from second_number (digit2)."""
        # Insert zeros at the beginning of the current result based on the current digit's place.
        current_result = [0] * num_zeros
        carry = 0

        # Multiply each digit in first_number with the current digit of the second_number.
        for digit1 in first_number:
            multiplication = int(digit1) * int(digit2) + carry
            # Set carry equal to the tens place digit of multiplication.
            carry = multiplication // 10
            # Append last digit to the current result.
            current_result.append(multiplication % 10)

        if carry != 0:
            current_result.append(carry)
        return current_result

    def sum_results(self, results: List[List[int]]) -> List[int]:
        # Initialize answer as a number from results.
        answer = results.pop()

        # Add each result to answer one at a time.
        for result in results:
            new_answer = []
            carry = 0

            # Sum each digit from answer and result. Note: zip_longest is the
            # same as zip, except that it pads the shorter list with fillvalue.
            for digit1, digit2 in zip_longest(result, answer, fillvalue=0):
                # Add current digit from both numbers.
                curr_sum = digit1 + digit2 + carry
                # Set carry equal to the tens place digit of curr_sum.
                carry = curr_sum // 10
                # Append the ones place digit of curr_sum to the new answer.
                new_answer.append(curr_sum % 10)

            if carry != 0:
                new_answer.append(carry)

            # Update answer to new_answer which equals answer + result
            answer = new_answer

        return answer
    


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if "0" in [num1, num2]:
            return "0"
        
        res = [0] * (len(num1) + len(num2))
        num1, num2 = num1[::-1], num2[::-1]

        for i1 in range(len(num1)):
            for i2 in range(len(num2)):
                digit = int(num1[i1]) * int(num2[i2])
                res[i1 + i2] += digit
                res[i1 + i2 + 1] += (res[i1 + i2] // 10)
                res[i1 + i2] = res[i1 + i2] % 10
        res, beg = res[::-1], 0
        while beg < len(res) and res[beg] == 0:
            beg += 1

        res = map(str, res[beg:])
        return "".join(res)
    #TIME COMPLEXITY O(N1 * N2)
    #SPACE COMPLEXITYO(N1 + N2)
