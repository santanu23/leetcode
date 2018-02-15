class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        index_forward, index_backward = 0, len(numbers) - 1

        while index_forward < index_backward:
            s = numbers[index_forward] + numbers[index_backward]
            if s == target:
                return [index_forward+1, index_backward+1]
            elif s < target:
                index_forward += 1
            else:
                index_backward -= 1

        raise ValueError
