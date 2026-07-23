class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        
        for i in nums:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
        
        for n, c in count.items():
            freq[c].append(n)
        
        result = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                result.append(num)
                if len(result) == k:
                    return result

