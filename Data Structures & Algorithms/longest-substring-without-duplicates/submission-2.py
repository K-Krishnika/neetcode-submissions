class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r=0,0
        freq={}
        c=0
        while(r<len(s)):
            if s[r] in freq:
                l=max(l,freq[s[r]]+1)
                freq[s[r]]=r
                
            else:
                freq[s[r]]=r
            c=max(c,r-l+1)
            r+=1
            
        return c       
