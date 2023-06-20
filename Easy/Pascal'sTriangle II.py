from math import comb


class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        return [comb(rowIndex, i) for i in range(rowIndex + 1)]


if __name__ == '__main__':
    print(f'Example 1" {Solution().getRow(3)}\n'
          f'Example 2: {Solution().getRow(0)}\n'
          f'Example 3: {Solution().getRow(1)}')
