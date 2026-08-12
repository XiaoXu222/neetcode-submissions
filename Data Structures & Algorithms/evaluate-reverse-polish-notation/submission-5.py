import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {
            "+": operator.add,
            "-": operator.sub, 
            "*": operator.mul,
            "/": operator.truediv
        }
        stack = []
        for token in tokens:
            if token in operators:
                b = stack.pop()
                a = stack.pop()
                last = operators[token](a, b)
                stack.append(int(last))
            else:
                stack.append(int(token))

        return stack[0]

        