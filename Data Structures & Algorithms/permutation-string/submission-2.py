class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq={}
        for i in range(len(s1)):
            freq[s1[i]]=freq.get(s1[i],0)+1
        l,r=0,0
        dect=freq.copy()
        while(l<len(s2) and r<len(s2)):
            #print(s2[l],s2[r],dect)
            if s2[r] in dect.keys() and dect.get(s2[r])>0:
                dect[s2[r]]=dect.get(s2[r])-1
                r+=1
            else:
                l+=1
                r=l
                dect=freq.copy()
            if all(v == 0 for v in dect.values()):
                return True
                break
        return False