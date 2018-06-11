class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        operators = ["+","-","*","/"]
        
        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            else:
                l = stack.pop()
                r = stack.pop()
                if token == "+":
                    stack.append(r+l)
                elif token == "-":
                    stack.append(r-l)
                elif token == "*":
                    stack.append(r*l)
                elif token == "/":
                    stack.append(int(operator.truediv(r,l)))
        
        return stack[0]
