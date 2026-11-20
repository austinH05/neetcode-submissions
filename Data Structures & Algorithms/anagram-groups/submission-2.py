class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sol = defaultdict(list)
        
        for word in strs:
            count = [0] * 26
            for c in word:
                count[ord(c) - ord('a')] += 1
            sol[tuple(count)].append(word)

        
        res = []
        for key, value in sol.items():
            res.append(value)

        return res

                
