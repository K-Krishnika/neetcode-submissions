class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r=0,len(heights)-1
        res=0
        while(l<r):
            x=min(heights[l],heights[r])*(r-l)
            res=max(res,x)
            if heights[l]<heights[r]:
                l+=1
            elif heights[r]<heights[l]:
                r-=1
            elif heights[r-1]<heights[l-1]:
                l+=1
            else:
                r-=1
        return res
        