def reverse(self, x):
        """
        :type x: int
        :rtype: int 
        """
        temp = 0
        if x < 0:
            x = -x
        while x != 0:
            
            rev_num = 0
            rev_num = rev_num*10 + x%10
            if (rev_num - x)//10  != temp:
                return 0
            temp = rev_num
            x = x//10
        return rev_num
