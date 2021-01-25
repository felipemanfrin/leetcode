from typing import List


class Solution:
    def mostCompetitive(nums: List[int], k: int) -> List[int]:
        # mono increasing stack
        stack = []
        n = len(nums)
        for i, num in enumerate(nums):
            while stack and stack[-1] > num and len(stack) + n - i > k:
                stack.pop()

            if len(stack) < k:
                stack.append(num)
        return stack



    print(mostCompetitive(nums = [3,5,2,6], k = 2))
