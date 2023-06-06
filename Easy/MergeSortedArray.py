class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        nums1[m:] = nums2[:n]
        nums1.sort()


if __name__ == '__main__':
    nums1, m1, nums2, n1 = [1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3
    nums3, m2, nums4, n2 = [1], 1, [], 0
    nums5, m3, nums6, n3 = [0], 0, [1], 1

    Solution().merge(nums1, m1, nums2, n1)
    Solution().merge(nums3, m2, nums4, n2)
    Solution().merge(nums5, m3, nums6, n3)
    print(f'Example 1: {nums1}\n'
          f'Example 2: {nums3}\n'
          f'Example 3: {nums5}')
