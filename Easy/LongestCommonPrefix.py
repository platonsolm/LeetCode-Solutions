from itertools import takewhile


class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        return ''.join(a[0] for a in takewhile(lambda x: len(set(x)) == 1, zip(*strs)))


if __name__ == '__main__':
    print(f'Example 1: {Solution().longestCommonPrefix(["flower", "flow", "flight"])}\n'
          f'Example 2: {Solution().longestCommonPrefix(["dog", "racecar", "car"])}')
