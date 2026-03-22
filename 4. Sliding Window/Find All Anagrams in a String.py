class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        if len(p) > len(s):
            return []
        
        p_count = {}
        window_count = {}
        
        # build initial window
        for i in range(len(p)):
            p_count[p[i]] = 1 + p_count.get(p[i], 0)
            window_count[s[i]] = 1 + window_count.get(s[i], 0)
        
        result = []
        
        # check first window
        if p_count == window_count:
            result.append(0)
        
        left = 0
        
        for right in range(len(p), len(s)):
            
            # add new char
            window_count[s[right]] = 1 + window_count.get(s[right], 0)
            
            # remove old char
            window_count[s[left]] -= 1
            if window_count[s[left]] == 0:
                del window_count[s[left]]
            
            left += 1
            
            # check match
            if window_count == p_count:
                result.append(left)
        
        return result
