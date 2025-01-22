class Solution(object):      
    def romanToInt(self, s):
        def value(c):
            if(c=="I"):
                return 1
            elif(c=="V"):
                return 5
            elif(c=="X"):
                return 10
            elif(c=="L"):
                return 50
            elif(c=="C"):
                return 100
            elif(c=="D"):
                return 500
            elif(c=="M"):
                return 1000
        """
        :type s: str
        :rtype: int
        """
        l=list(s)
        sum=0
        i=0
        while i<len(l):
            if(i+1<len(l) and value(l[i])<value(l[i+1])):
                sum=sum+value(l[i+1])-value(l[i])
                i=i+2
            else:
                sum=sum+value(l[i])
                i=i+1
        return sum
            
            
