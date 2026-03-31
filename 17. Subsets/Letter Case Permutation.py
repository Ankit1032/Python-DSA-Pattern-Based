class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        
        '''
        Following the subset logic where each letter has 2 choices
        '''

        res = []
        path = []

        def backtrack(i):

            if i == len(s):
                res.append("".join(path)) # "".join(path) -> because we want string
                return

            if s[i].isalpha():
                #Lowercase
                path.append(s[i].lower())
                backtrack(i+1)
                path.pop()

                #Uppercase
                path.append(s[i].upper())
                backtrack(i+1)
                path.pop()

            else: #digit -> 1 choice
                path.append(s[i])
                backtrack(i+1)
                path.pop()
        
        backtrack(0)
        return res
