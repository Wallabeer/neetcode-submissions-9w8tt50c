class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        
        dict_s = {}
        dict_t = {}

        for char in s:
            if char in dict_s:
                dict_s[char] = dict_s[char] + 1
            else:
                dict_s[char] = 1
        
        for char in t:
            if char in dict_t:
                dict_t[char] = dict_t[char] + 1
            else:
                dict_t[char] = 1
        
        for key, value in dict_s.items():
            if dict_t.get(key, -1) != value:
                return False
        
        # for key, value in dict_t.items():
        #     if dict_s.get(key, -1) != value:
        #         return False
        
        return True