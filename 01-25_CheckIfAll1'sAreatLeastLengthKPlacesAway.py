from typing import List

class Solution:
    def kLengthApart(nums: List[int], k: int) -> bool:
        pos = k
        for i in range(len(nums)):
            if nums[i] == 1:
                if pos < k:
                    return False
                pos = 0
            else:
                pos += 1
        return True










    print(kLengthApart(nums = [1,0,0,0,1,0,0,1], k = 2))
