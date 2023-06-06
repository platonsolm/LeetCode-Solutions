class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]


if __name__ == '__main__':
    print(f'Example 1: {Solution().addBinary("11", "1")}\n'
          f'Example 2: {Solution().addBinary("1010", "1011")}')
