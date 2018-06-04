class Solution(object): 
    def letterCasePermutation(self, S):
        numbers = [str(i) for i in range(0,10)]
        """
        :type S: str
        :rtype: List[str]
        """
        if len(S) == 0:
            return [""]
        
        if len(S) == 1:
            if S[0] in numbers:
                return [S]
            else:
                return [S.lower(),S.upper()]
            
        res = set()
        for combination in self.letterCasePermutation(S[1:]):
            res.add(S[0].upper() + combination)
            res.add(S[0].lower() + combination)
        
        return list(res)
