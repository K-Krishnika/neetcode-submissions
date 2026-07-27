class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        freq={}
        val=0
        for r in range(len(s)):
            freq[s[r]]=freq.get(s[r],0)+1
            
            m=max(freq.values())
            if r-l+1-m>k:
                freq[s[l]]=freq.get(s[l],1)-1
                l+=1
            val=max(val,r-l+1)
        return val