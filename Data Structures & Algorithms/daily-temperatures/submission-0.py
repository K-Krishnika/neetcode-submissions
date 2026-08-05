class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res=[0]*len(temperatures)
        for i in range(len(temperatures)):
            x=temperatures[i]
            count=0
            for j in range(i,len(temperatures)):
                if x<temperatures[j]:
                    res[i]=count
                    break
                count+=1
        return res

