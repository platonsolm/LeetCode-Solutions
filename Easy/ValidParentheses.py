class Solution:
    def isValid(self, s: str) -> bool:
        chars, brackets = [], {')': '(', '}': '{', ']': '['}
        for char in s:
            if brackets.__contains__(char):
                if not chars or chars.pop() != brackets.__getitem__(char):
                    return False
            else:
                chars.append(char)
        return 0 == len(chars)


if __name__ == '__main__':
    print(f'Example 1: {Solution().isValid("()")}\n'
          f'Example 2: {Solution().isValid("()[]{}")}\n'
          f'Example 3: {Solution().isValid("(]")}')
