from typing import List

class Solution:
    def maxOperations(nums: List[int], k: int) -> int:
        nums.sort()
        count = 0
        i, j = 0, len(nums)-1

        while i < j:
            total = nums[i] + nums[j]
            if total == k:
                i += 1
                j -= 1
                count += 1
            elif total > k:
                j -= 1
            else:
                i +=1
        return count
    print(maxOperations(nums = [1,2,3,4], k = 5))
