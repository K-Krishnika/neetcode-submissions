class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)<=1:
            return len(nums)
        num=set(nums)
        res=0
        print(num)
        nums=list(num)
        nums.sort()
        tc=1
        for i in range(1,len(nums)):
            if nums[i]-nums[i-1]==1:
                tc+=1
            else:
                res=max(res,tc)
                tc=1
        res=max(res,tc)
        return res