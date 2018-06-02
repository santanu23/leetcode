class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for c in s:
            if c == "(" or c == "{" or c == "[":
                stack.append(c)
            else:
                if stack and \
                   (stack[-1] == "{" and c == "}" or \
                    stack[-1] == "[" and c == "]" or \
                    stack[-1] == "(" and c == ")"):
                    stack.pop()
                else:
                    return False
        
        return len(stack) == 0
