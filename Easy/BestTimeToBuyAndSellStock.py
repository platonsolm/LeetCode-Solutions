class Solution:
    def max_profit(self, prices: list[int]) -> int:
        min_price, max_profit = max(prices), 0
        for price in prices:
            min_price = min(min_price, price)
            profit = price - min_price
            max_profit = max(max_profit, profit)
        return max_profit


if __name__ == '__main__':
    print(f'Example 1: {Solution().max_profit([7, 1, 5, 3, 6, 4])}\n'
          f'Example 2: {Solution().max_profit([7, 6, 4, 3, 1])}')
