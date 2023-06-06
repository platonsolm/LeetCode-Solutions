class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        return nums.index(target) if target in nums else sorted(nums + [target]).index(target)


if __name__ == '__main__':
    print(f'Example 1: {Solution().searchInsert([1, 3, 5, 6], 5)}\n'
          f'Example 2: {Solution().searchInsert([1, 3, 5, 6], 2)}\n'
          f'Example 3: {Solution().searchInsert([1, 3, 5, 6], 7)}')
