class Solution:
    def isValid(self, s: str) -> bool:
        bracket_map = {")": "(", "}": "{", "]": "["}
        stack = []
        
        for char in s:
            # If it's a closing bracket
            if char in bracket_map:
                # Pop the top element if stack isn't empty; else assign a dummy value
                top_element = stack.pop() if stack else '#'
                
                # If the mapping doesn't match the stack's top element, it's invalid
                if bracket_map[char] != top_element:
                    return False
            else:
                # It's an opening bracket, push it onto the stack
                stack.append(char)
                
        # The string is valid only if the stack is completely empty
        return not stack        