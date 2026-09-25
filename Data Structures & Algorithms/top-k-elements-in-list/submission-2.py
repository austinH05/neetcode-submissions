class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for n in nums: 
            hashmap[n] = hashmap.get(n, 0) + 1
        
        freq = [[] for i in range(len(nums) + 1)]
        for num, count in hashmap.items():
            freq[count].append(num) 

        solution = []
        for i in range(len(freq) -1, 0, -1):
            for num in freq[i]:
                solution.append(num)
                if len(solution) == k:
                    return solution