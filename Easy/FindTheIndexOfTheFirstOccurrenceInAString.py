class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)


if __name__ == '__main__':
    print(f'Example 1: {Solution().strStr("sadbutsad", "sad")}\n'
          f'Example 2: {Solution().strStr("leetcode", "leeto")}')
