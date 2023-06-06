from math import comb


class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        return [[comb(j, i) for i in range(j + 1)] for j in range(numRows)]


if __name__ == '__main__':
    print(f'Example 1: {Solution().generate(5)}\n'
          f'Example 2: {Solution().generate(1)}')
