class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        r=[]
        car=sorted(zip(position,speed),reverse=True)
        for i, j in car:
            r.append((target-i)/j)
        res=[]
        res.append(r[0])
        for i in range(1,len(r)):
            if res[-1]<r[i]:
                res.append(r[i])
        return len(res)

        
    