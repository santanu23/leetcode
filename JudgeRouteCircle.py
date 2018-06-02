class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        lr_count = 0
        ud_count = 0
        for move in moves:
            if move == 'U':
                ud_count += 1
            elif move == 'D':
                ud_count -= 1
            elif move == 'L':
                lr_count += 1
            elif move == 'R':
                lr_count -= 1

        if lr_count or ud_count:
            return False
        return True
        
class Solution(object):
  def judgeCircle(self, moves):
      return moves.count('L') == moves.count('R') and moves.count('U') == moves.count('D')
