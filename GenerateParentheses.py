class Solution(object):
    def generateParenthesis(self,n):
        """
        :type n: int
        :rtype: List[str]
        """
        all_possible_perms = self.helper(2*n)
        return list(filter(self.validate_parens,all_possible_perms))

    def helper(self,n):
        if n == 1:
            return ["(",")"]

        res = []

        for combination in self.helper(n-1):
            res.append(combination+"(")
            res.append(combination+")")

        return res

    def validate_parens(self,paren):
        count = 0
        for i in range(len(paren)):
            if paren[i] == "(":
                count += 1
            else:
                count -= 1
                if count < 0:
                    return False

        return count == 0
