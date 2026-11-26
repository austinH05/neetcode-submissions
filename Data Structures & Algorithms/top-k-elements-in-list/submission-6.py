class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = {}

        for num in nums:
            hm[num] = hm.get(num, 0) + 1
        
        freq = [[] for i in range(len(nums) + 1)]

        for key, value in hm.items():
            freq[value].append(key)
        
        res = []
        for i in range(len(freq) - 1, -1, -1):
            for num in freq[i]:
                if len(res) < k:
                    res.append(num)
        
        return res
        