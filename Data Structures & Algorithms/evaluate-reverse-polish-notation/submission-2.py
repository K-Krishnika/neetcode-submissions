import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        op={"+":operator.add,
        "-":operator.sub,
        "*": operator.mul,
        "/": lambda a,b: int(a/b)}
        for i in tokens:
            if i in op:
                a=stack.pop()
                b=stack.pop()
                cal=op[i]
                stack.append(cal(b,a))
            else:
                stack.append(int(i))
        return stack[-1]
        