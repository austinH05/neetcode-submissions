class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        for word in strs:
            string = string + word + "é"
            
        return string

    def decode(self, s: str) -> List[str]:
        sol = []
        word = ""
        for c in s:
            if c != "é":
                word += c
            else:
                sol.append(word)
                word = ""
        return sol
            