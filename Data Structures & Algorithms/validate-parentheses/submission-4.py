class Solution:
    def isValid(self, s: str) -> bool:
        brac={')': '(', '}': '{' , ']':'[' }
        stack=[]
        for i in s:
            if i in brac:
                
                last=stack.pop() if stack else "#"

                if last!=brac[i]:
                    return False
                else:
                    continue
            stack.append(i)
            print(stack)
        return not stack