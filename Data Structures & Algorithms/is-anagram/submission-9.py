class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hm1, hm2 = {}, {}

        for x in range(len(s)):
            hm1[s[x]] = hm1.get(s[x], 0) + 1
            hm2[t[x]] = hm2.get(t[x], 0) + 1

        return hm1 == hm2