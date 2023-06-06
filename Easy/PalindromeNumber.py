class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]


if __name__ == '__main__':
    print(f'Example 1: {Solution().isPalindrome(121)}\n'
          f'Example 2: {Solution().isPalindrome(-121)}\n'
          f'Example 3: {Solution().isPalindrome(10)}')
