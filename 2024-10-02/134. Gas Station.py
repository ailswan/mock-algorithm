from typing import List

# 134. Gas Station

# There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].

# You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.

# Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique.

 

# Example 1:

# Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
# Output: 3
# Explanation:
# Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
# Travel to station 4. Your tank = 4 - 1 + 5 = 8
# Travel to station 0. Your tank = 8 - 2 + 1 = 7
# Travel to station 1. Your tank = 7 - 3 + 2 = 6
# Travel to station 2. Your tank = 6 - 4 + 3 = 5
# Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
# Therefore, return 3 as the starting index.
# Example 2:

# Input: gas = [2,3,4], cost = [3,4,3]
# Output: -1
# Explanation:
# You can't start at station 0 or 1, as there is not enough gas to travel to the next station.
# Let's start at station 2 and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
# Travel to station 0. Your tank = 4 - 3 + 2 = 3
# Travel to station 1. Your tank = 3 - 3 + 3 = 3
# You cannot travel back to station 2, as it requires 4 unit of gas but you only have 3.
# Therefore, you can't travel around the circuit once no matter where you start.
 

# Constraints:

# n == gas.length == cost.length
# 1 <= n <= 105
# 0 <= gas[i], cost[i] <= 104\

class Solution:
    def gasStation(self, gas: List[int], cost: List[int]) -> int:
        # Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
        # a - > b - > c  
        # 0    1     2

    #         start       i 
        # gas[i] - cost[i] > 0 get the possible of start i
        # pre_sum_gas[start: i] >= pre_sum_cost[start: i] else: move i
        n = len(gas)
        pre_sum_gas = 0
        pre_sum_cost = 0
        start = 0
        i = 0
        # Input: gas = [2,3,4], cost = [3,4,3]\
        #2   3  4
        #3   4  3
        #    i  s
        # Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
        # 1,2,3,4,5
        # 3,4,5,1,2
        #     i s   
        iscycle = False
        while i < n and iscycle == False: # i= 3 < 5
            if gas[i] - cost[i] < 0:
                pre_sum_gas = 0
                pre_sum_cost = 0
                i += 1
                continue
            start = i# 3
            pre_sum_gas += gas[i]  
            pre_sum_cost += cost[i]
            while pre_sum_gas >= pre_sum_cost:# 15 >= 15
                i += 1 # 3
                if i >= n:# 3 >= 5?
                    i %= n # 0
                    iscycle = True  # True
                if i >= start and iscycle == True:# 3 >= 3  True?
                    return start  # 3
                pre_sum_gas += gas[i] # 9 + 1 + 2 + 3
                pre_sum_cost += cost[i]# 3 + 3 + 4 + 5
        return -1

#time complexity O(n)
#space complexity O(1)



class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_gain = 0
        curr_gain = 0
        answer = 0
        #  3  0   0   3   9
        #  2  2   2   3   2
        #             i
        for i in range(len(gas)):
            # gain[i] = gas[i] - cost[i]
            total_gain += gas[i] - cost[i]
            curr_gain += gas[i] - cost[i]

            # If we meet a "valley", start over from the next station
            # with 0 initial gas.
            if curr_gain < 0:
                curr_gain = 0
                answer = i + 1

        return answer if total_gain >= 0 else -1