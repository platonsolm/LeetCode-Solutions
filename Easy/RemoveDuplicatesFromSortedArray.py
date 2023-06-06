class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        nums[:] = sorted(set(nums))
        return len(nums)


if __name__ == '__main__':
    print(f'Example 1: {Solution().removeDuplicates([1, 1, 2])}\n'
          f'Example 2: {Solution().removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4])}')
