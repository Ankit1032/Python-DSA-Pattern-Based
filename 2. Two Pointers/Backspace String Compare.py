class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        # My solution with Stacks ###########################################################
        # stack_s = []
        # stack_t = []

        # for i in s:
        #     if i != '#':
        #         stack_s.append(i)
        #     elif stack_s: #incase stack if empty "##" else it will give runtime error
        #         stack_s.pop()

        # for i in t:
        #     if i != '#':
        #         stack_t.append(i)
        #     elif stack_t: #incase stack is empty
        #         stack_t.pop()

        # return stack_s == stack_t

        # My solution with Two Pointer ######################################################
        # right_s = len(s)-1
        # right_t = len(t)-1

        # s_hash_counter = 0
        # t_hash_counter = 0

        # while right_s >= 0 or right_t >= 0: #if we use 'and' then loop will stop if one finishes so we shuld use 'or'
            
            
        #     if right_s >= 0 and s[right_s] =='#': #counting # in s #keeping this condition(right_s >= 0) because we are using 'or' in while loop
        #         s_hash_counter += 1
        #         right_s -= 1
        #     elif right_t >= 0 and t[right_t] =='#': #counting # in t #keeping this condition(right_t >= 0) because we are using 'or' in while loop
        #         t_hash_counter += 1
        #         right_t -= 1
        #     elif right_s >= 0 and s[right_s] != '#' and s_hash_counter > 0: #skipping 's' letters due to #
        #         right_s -= 1
        #         s_hash_counter -= 1
        #     elif right_t >= 0 and t[right_t] != '#' and t_hash_counter > 0: #skipping 's' letters due to #
        #         right_t -= 1
        #         t_hash_counter -= 1
        #     elif right_s >= 0 and right_t >= 0 and s[right_s] != '#' and t[right_t] != '#' and s_hash_counter == 0 and t_hash_counter == 0 and s[right_s] != t[right_t]:
        #         return False
        #     elif right_s >= 0 and right_t >= 0 and s[right_s] != '#' and t[right_t] != '#' and s_hash_counter == 0 and t_hash_counter == 0 and s[right_s] == t[right_t]: #all condition match | True match
        #         right_s -= 1
        #         right_t -= 1
        #     # s exhausted but t still has valid char (no pending hashes)
        #     elif right_t >= 0 and t_hash_counter == 0:
        #         return False
        #     # t exhausted but s still has valid char (no pending hashes)  
        #     elif right_s >= 0 and s_hash_counter == 0:
        #         return False

        # return True

        # Neetcode solution #################################

        def nextValidCharacter(str, index):
            
            backspace = 0

            # Below didnt work because backspace > 0 has bug as we aint checking if it contain a valid character as # can also be present 
            # while index >= 0:
            #     if backspace == 0 and str[index] != '#':
            #         break
            #     elif backspace > 0:
            #         index -= 1
            #         backspace -= 1
            #     elif str[index] == '#':
            #         backspace += 1
            #         index -= 1

            while index>=0:
                if backspace == 0 and str[index] != '#':
                    break
                elif str[index] == '#':
                    backspace += 1
                    index -= 1
                elif backspace > 0:
                    index -= 1
                    backspace -= 1


            return index

        index_s , index_t = len(s)-1, len(t)-1

        while index_s >= 0 or index_t >= 0: #we dont use 'and' because this loop will break if one string is exhausted and the other string still contains  letters and #s. So we exhaust these both string using 'or' so that our (char_s) != (char_t) will compare and return false
            index_s = nextValidCharacter(s, index_s)
            index_t = nextValidCharacter(t, index_t)

            #to handle out of bound conditions
            char_s = s[index_s] if index_s >= 0 else ""
            char_t = t[index_t] if index_t >= 0 else ""

            if char_s != char_t:
                return False
            index_s -= 1
            index_t -= 1
        
        return True
