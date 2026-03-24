class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        mapping = {
            '(':')',
            '{':'}',
            '[':']'
        }

        for i in range(len(s)):
            if s[i] in mapping.keys():
                stack.append(s[i])
            else:
                if not stack or mapping[stack[-1]] != s[i]: #we check 'not stack' because what if the first char is closed bracket then stack will always be empty
                    return False
                stack.pop()  

        if stack == []: #what if we had only "[" --> so in that case, this condition is required
            return True
        return False
