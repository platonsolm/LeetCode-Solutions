class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])


if __name__ == '__main__':
    print(f'Example 1: {Solution().lengthOfLastWord("Hello World")}\n'
          f'Example 2: {Solution().lengthOfLastWord("   fly me   to   the moon  ")}\n'
          f'Example 3: {Solution().lengthOfLastWord("luffy is still joyboy")}')
