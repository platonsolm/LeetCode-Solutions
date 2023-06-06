class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        return list(map(int, str(int(''.join(str(i) for i in digits)) + 1)))


if __name__ == '__main__':
    print(f'Example 1: {Solution().plusOne([1, 2, 3])}\n'
          f'Example 2: {Solution().plusOne([4, 3, 2, 1])}\n'
          f'Example 3: {Solution().plusOne([9])}')
