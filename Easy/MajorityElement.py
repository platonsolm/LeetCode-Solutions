class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        return sorted(nums)[len(nums) // 2]


if __name__ == '__main__':
    print(f'Example 1: {Solution().majorityElement([3, 2, 3])}\n'
          f'Example 2: {Solution().majorityElement([2, 2, 1, 1, 1, 2, 2])}\n')
