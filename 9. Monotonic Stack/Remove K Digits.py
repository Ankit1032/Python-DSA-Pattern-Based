class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        
        stack = []
        
        for digit in num:
            
            while stack and k > 0 and stack[-1] > digit: #we always want lesser number values in front of the digits
                stack.pop()
                k -= 1
            
            stack.append(digit)
        
        # if k still remains → remove from end #[1,2,3,4,5] in this case, K will remain so remove from last as bigger numbers are at last
        while k > 0:
            stack.pop()
            k -= 1
        
        # build result
        result = "".join(stack)
        
        # remove leading zeros
        result = result.lstrip('0')
        
        return result if result else "0"
