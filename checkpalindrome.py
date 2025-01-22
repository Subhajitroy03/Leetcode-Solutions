class Solution(object):
    def isPalindrome(self, x):
        temp2=str(x)
        if(temp2[::-1]==str(x)):
            return True
        else:
            return False
