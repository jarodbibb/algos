class Solution(object):
    def reverse(self, x):


        pos_x = abs(x)
        reverse = 0 
        while pos_x != 0:
            reminder = pos_x % 10
            reverse = reverse * 10 + reminder
            pos_x = pos_x // 10
        if reverse > pow(2,31):
            return 0
        return reverse if x > 0 else reverse*-1
        