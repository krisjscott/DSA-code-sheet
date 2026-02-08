class Solution:
    def minCost(self, nums, cost) -> int:
        pairs = (list(i) for i in zip(nums,cost))
        print(list(pairs))

obj = Solution()
obj.minCost([100, 1, 50, 2],[5, 1, 1, 10])