class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        '''
        My first intuition is to create the bracket list and then use same permutation code and it was WRONG because
        question asked for "Well Formed Parenthesis"
        '''

        # bracket = []

        # #1) Make the list of brackets
        # for i in range(n):
        #     bracket.append("(")

        # for i in range(n):
        #     bracket.append(")")

        # br_len = n*2
        
        # #2) Use permutation code

        # res = []
        # used = [False] * (br_len) #n*2 is the size of the bracket array
        # path = []

        # def backtrack():
            
        #     if len(path) == br_len:
        #         res.append("".join(path))
        #         return
            
        #     for i in range(br_len):

        #         if used[i]:
        #             continue
                
        #         #Used
        #         path.append(bracket[i])
        #         used[i] = True

        #         backtrack()

        #         #Unused
        #         path.pop()
        #         used[i] = False


        # backtrack()
        # return res 

        ### Solution 2 - ChatGPT

        '''
        Condition to add open bracket:
        1. We can only add 'n' number of open brackets

        Condition to add close bracket:
        1. We will only add close bracket if it is lesser than open bracket and close bracket cannot be more then 'n
        '''

        res = []

        def backtrack(openBracket, closeBracket, path):
            if openBracket == n and closeBracket == n:
                res.append(path)

            #Add '('
            if openBracket < n:
                backtrack(openBracket+1, closeBracket, path + '(')

            #Add ')'
            if closeBracket < openBracket:
                backtrack(openBracket, closeBracket+1, path + ')')

        backtrack(0,0,"")

        return res
            

