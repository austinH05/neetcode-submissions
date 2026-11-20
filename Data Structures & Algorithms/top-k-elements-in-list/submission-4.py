class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = {}

        for x in nums:
            hm[x] = hm.get(x, 0) + 1
        
        freqs = [[] for i in range (len(nums) + 1)]
        for num, freq in hm.items():
            freqs[freq].append(num)
        
        res = []
        for x in range(len(freqs) - 1, 0, -1):
            for num in freqs[x]:
                if len(res) < k:
                    res.append(num)

        return res
        
    