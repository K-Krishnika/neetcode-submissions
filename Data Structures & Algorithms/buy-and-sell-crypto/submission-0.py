class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini=prices[0]
        pro=0
        for i in prices:
            pro=max(pro,i-mini)
            mini=min(mini,i)
        return pro