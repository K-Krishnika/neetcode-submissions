class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()
        for i in range(len(nums)):
            now=-nums[i]
            l,r=0,len(nums)-1
            while l<r and i!=l and i!=r:
                x=nums[l]+nums[r]
                if x==now:
                    res.append([nums[i],nums[l],nums[r]])
                    while l<r and nums[l]==nums[l+1]:
                        l+=1
                    while l<r and nums[r]==nums[r-1]:
                        r-=1
                    l+=1
                    r-=1
                elif x<now:
                    l+=1
                else:
                    r-=1
        fin=[]
        for i in res:
            i.sort()
            if i not in fin:
                fin.append(i)
        
        return fin