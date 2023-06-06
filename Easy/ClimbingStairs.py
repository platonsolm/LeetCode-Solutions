class Solution:
    def climbStairs(self, n: int) -> int:
        a, b = [1] * 2
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b


if __name__ == '__main__':
    print(f'Example 1: {Solution().climbStairs(2)}\n'
          f'Example 2: {Solution().climbStairs(3)}')
