# 1672. Richest Customer Wealth

class Solution(object):
    # def maximumWealth(self, accounts):
    #     rich_list = []
    #     for i in (accounts):
    #         rich_list.append(sum(i))
    #     return (max(rich_list))

    def maximumWealth(self, accounts):
        return max([sum(i) for i in accounts])

