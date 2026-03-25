class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        
        
        stack = []  # (char, count)
        
        for ch in s:
            
            if stack and stack[-1][0] == ch:
                stack[-1][1] += 1
            else:
                stack.append([ch, 1])
            
            # if count reaches k → remove
            if stack[-1][1] == k:
                stack.pop()
        
        # rebuild string
        result = []
        for ch, count in stack:
            result.append(ch * count)
        
        return "".join(result)

        '''
        Dry Run: #"deeedbbcccbdaa"
        [['d', 1]]
        ===============
        [['d', 1], ['e', 1]]
        ===============
        [['d', 1], ['e', 2]]
        ===============
        [['d', 1]]
        ===============
        [['d', 2]]
        ===============
        [['d', 2], ['b', 1]]
        ===============
        [['d', 2], ['b', 2]]
        ===============
        [['d', 2], ['b', 2], ['c', 1]]
        ===============
        [['d', 2], ['b', 2], ['c', 2]]
        ===============
        [['d', 2], ['b', 2]]
        ===============
        [['d', 2]]
        ===============
        []
        ===============
        [['a', 1]]
        ===============
        [['a', 2]]
        ===============

        '''
