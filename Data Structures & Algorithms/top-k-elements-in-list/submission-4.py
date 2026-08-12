class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num,0)
        freq_sort = [[] for i in range(len(nums)+1)]
        num_freq = list(count.items())
        for i in range(len(num_freq)):
            pair = num_freq[i]
            freq_sort[pair[1]].append(pair[0])
        
        top_k = []
        for i in range(len(nums),0,-1):
            for num in freq_sort[i]:
                top_k.append(num)
                if len(top_k) == k:
                    return top_k
        
        