from string import ascii_uppercase


class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans = ''
        while columnNumber:
            columnNumber -= 1
            ans = ascii_uppercase[columnNumber % 26] + ans
            columnNumber //= 26
        return ans


if __name__ == '__main__':
    print(f'Example 1: {Solution().convertToTitle(1)}\n'
          f'Example 2: {Solution().convertToTitle(28)}\n'
          f'Example 3: {Solution().convertToTitle(701)}')
