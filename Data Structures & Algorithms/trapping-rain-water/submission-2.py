class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        level=0
        left,right=[],[]
        l,r=0,len(height)-1
        ma=height[0]
        while l<len(height):
            ma=max(ma,height[l])
            left.append(ma)
            l+=1
        
        ma=height[len(height)-1]
        while r>=0:
            ma=max(ma,height[r])
            right.append(ma)
            r-=1
        right=right[::-1]
        for i in range(len(height)):
            level+=min(right[i],left[i])-height[i]
        return level