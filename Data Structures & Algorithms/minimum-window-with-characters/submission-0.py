class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freq={}
        for i in range(len(t)):
            freq[t[i]]=freq.get(t[i],0)+1
        l,r=0,0 
        ll=float('inf'), None, None       
        while(l<len(s) and r<len(s)):
            if s[r] in freq:
                freq[s[r]]=freq.get(s[r])-1           
            if all(val<=0 for val in freq.values()):
           
                flag=True
                while(flag):
                    if r-l+1<ll[0]:
                        ll=r-l+1,l,r 
                    if s[l] in freq:
                        freq[s[l]]+=1
                        if freq[s[l]]>0:
                            flag=False
                    l+=1
            r+=1
        return "" if ll[1] is None else s[ll[1]:ll[2]+1]