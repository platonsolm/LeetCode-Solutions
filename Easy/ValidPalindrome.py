from string import punctuation


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join([i.lower() for i in s if not punctuation.__contains__(i)]).replace(' ', '')
        return s == s[::-1]


if __name__ == '__main__':
    print(f'Example 1: {Solution().isPalindrome("A man, a plan, a canal: Panama")}\n'
          f'Example 2: {Solution().isPalindrome("race a car")}\n'
          f'Example 3: {Solution().isPalindrome(" ")}')
