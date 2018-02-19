class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        x = str(x)
        min_int = -2147483648
        max_int = 2147483647

        if x[0] == '-':
            return 0 if int("-" + x[1:][::-1]) < min_int else int("-" + x[1:][::-1])
        else:
            return 0 if int(x[::-1]) > max_int else int(x[::-1])
