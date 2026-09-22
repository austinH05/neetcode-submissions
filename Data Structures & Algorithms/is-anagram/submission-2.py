class Solution:
    def isAnagram(self, s, t) -> bool:
        s1 = sorted(s)
        s2 = sorted(t)
        
        return s1 == s2