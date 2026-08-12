class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        paraMap = {"{": "}", "[": "]", "(": ")"}

        stack = []
        for para in s:
            if para in paraMap:
                stack.append(para)
            elif para not in paraMap: 
                if stack and paraMap[stack[-1]] == para:
                    stack.pop()
                else:
                    return False
        
        
        return True if not stack else False
        