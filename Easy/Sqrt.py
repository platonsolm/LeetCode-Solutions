class Solution:
    def mySqrt(self, x: int) -> int:
        return int(pow(x, 0.5))


if __name__ == '__main__':
    print(f'Example 1: {Solution().mySqrt(4)}\n'
          f'Example 2: {Solution().mySqrt(8)}')
