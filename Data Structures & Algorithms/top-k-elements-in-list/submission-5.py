class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = {}
        for num in nums:
            hm[num] = hm.get(num, 0) + 1
        
        freq = [[] for x in range(len(nums) + 1)]
        for key, value in hm.items():
            freq[value].append(key)

        res = []
        for x in range(len(freq) - 1, 0, -1):
            for num in freq[x]:
                if len(res) < k:
                    res.append(num)

        return res
        
    