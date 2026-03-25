class Solution:
    def removeDuplicates(self, s: str) -> str:

        if s == "":
            return s

        stack = []

        for i in s:
            if stack and i == stack[-1]:
                stack.pop()
            else:
                stack.append(i)
        
        return "".join(stack)

