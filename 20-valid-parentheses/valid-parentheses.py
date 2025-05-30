class Solution:
    # abhi
    def isValid(self, s: str) -> bool:
        stack=[]
        stack_mapping={"}":"{","]":"[",")":"("} # dictionary
        opening_stack=set(["(","[","{"])
        for x in s:
            if x in opening_stack:
                stack.append(x)
            elif stack and stack[-1] == stack_mapping[x]:
                stack.pop()
            else:
                return False
        if stack:
            return False
        else:
            return True                    

        