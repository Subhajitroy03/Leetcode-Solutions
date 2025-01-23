class Solution(object):
    def isValid(self, s):
        stack=[]
        for i in s:
            if(len(stack)==0):
                stack.append(i)
            elif(i in "({["):
                stack.append(i)
            elif(i in ")}]"):
                if((stack[-1]+i) in ["()","{}","[]"]):
                    stack.pop()
                else:
                    return False
        if(len(stack)==0):
            return True
        else:
            return False
