class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        num = 0
        for i in columnTitle:
            num = num * 26 + (ord(i) - ord('A') + 1)
        return num


if __name__ == '__main__':
    print(f'Example 1: {Solution().titleToNumber("A")}\n'
          f'Example 2: {Solution().titleToNumber("AB")}\n'
          f'Example 3: {Solution().titleToNumber("ZY")}')
