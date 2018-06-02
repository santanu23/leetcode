class Solution(object):
    
    def __init__(self):
        self.digit_map = ["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        if len(digits) == 1:
            return [l for l in self.digit_map[digits[0]]]
                
        res = []
        
        for combination in self.letterCombinations(digits[1:])
            for l in self.digit_map[digits[0]]:
                res.append(l + combination)
        
        return res
