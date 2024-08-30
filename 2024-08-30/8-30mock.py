from typing import List

#source ="facebook", target="fee" return 2
#source = "facebook", target="BOO" return 1

#constraints:
# case insensitive
# return 0 if target cannot be formed
import math
class Solution:
    def stickers(self, source: str, target: str) -> int:
        # get a count of all the characters in source input
        # get a count of all the chars in target
        # iterate through keys in target and see if the source char count is enough to satisfy target
            # if not, increment answer until it satisfies
        # return 1 if everything is satisfied

        # make inputs lowercase
        lower_source = source.lower()
        lower_target = target.lower()
        source_counts = Counter(lower_source)
        target_counts = Counter(lower_target)
        ans = 0

        for k, v in target.items():
            if k not in source_counts:
                return -1
            else:
                multiple = math.ceil(v / source_counts) #  1
                ans = max(ans, multiple)
        
        return ans
# time => O(n + 2m) where n is the length of source and m is the length of target; when n is significantly larger, then O(n)
# space => O(n + m) where n is length of source and m is length of target
#n + m + k   -> 