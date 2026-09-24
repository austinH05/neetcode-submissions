class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
      solution = defaultdict(list)
      for s in strs:
         count = [0] * 26
         for l in range(len(s)):
            count[ord(s[l]) - ord('a')] += 1
         solution[tuple(count)].append(s)
      return list(solution.values()) 
                
        