class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        for num in nums:
            if nums.count(num) != 2:
                return num


print(f'Example 1: {Solution().singleNumber([2, 2, 1])}\n'
      f'Example 2: {Solution().singleNumber([4, 1, 2, 1, 2])}\n'
      f'Example 3: {Solution().singleNumber([1])}')
