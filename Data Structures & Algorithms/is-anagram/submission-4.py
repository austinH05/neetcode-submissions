class Solution:
    def isAnagram(self, s, t) -> bool:
        
        if len(s) != len(t):
            return False

        count1 = {}
        count2 = {}

        for x in range (len(s)):
            count1[s[x]] = 1 + count1.get(s[x], 0)
            count2[t[x]] = 1 + count2.get(t[x], 0)
        return count1 == count2



        