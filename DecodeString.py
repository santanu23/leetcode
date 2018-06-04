class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        current_string = ""
        current_num = 0
        
        for char in s:
            if char == '[':
                stack.append(current_string)
                stack.append(current_num)
                current_string = ""
                current_num = 0
            elif char == ']':
                num = stack.pop()
                prevString = stack.pop()
                current_string = prevString + num*current_string
            elif char.isdigit():
                current_num = 10*current_num + int(char)
            else:
                current_string += char
            
        return current_string
