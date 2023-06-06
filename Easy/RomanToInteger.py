class Solution:
    def romanToInt(self, s: str) -> int:
        count, previous, romans = 0, 0, {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        for i in reversed(s):
            count, previous = count + romans[i] if romans[i] >= previous else count - romans[i], romans[i]
        return count


if __name__ == '__main__':
    print(f'Example 1: {Solution().romanToInt("III")}\n'
          f'Example 2: {Solution().romanToInt("LVIII")}\n'
          f'Example 3: {Solution().romanToInt("MCMXCIV")}')
