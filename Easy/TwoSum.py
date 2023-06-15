class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        num_dict = dict()
        for i, num in enumerate(nums):
            if target - num in num_dict:
                return [num_dict.get(target - num), i]
            num_dict.__setitem__(num, i)


if __name__ == '__main__':
    print(f'Example 1: {Solution().twoSum([2, 7, 11, 15], 9)}\n'
          f'Example 2: {Solution().twoSum([3, 2, 4], 6)}\n'
          f'Example 3: {Solution().twoSum([3, 3], 6)}')
