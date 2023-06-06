class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        nums[:] = [num for num in nums if num != val]
        return len(nums)


if __name__ == '__main__':
    print(f'Example 1: {Solution().removeElement([3, 2, 2, 3], 3)}\n'
          f'Example 2: {Solution().removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2)}')
