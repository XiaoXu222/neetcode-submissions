class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-stone for stone in stones]
        heapq.heapify(maxHeap)
        while len(maxHeap) > 1:
            y = -heapq.heappop(maxHeap)
            x = -heapq.heappop(maxHeap)
            # y = -maxHeap[0]
            # if len(maxHeap) > 2:
            #     x = max(-maxHeap[1], -maxHeap[2])
            # else:
            #     x = -maxHeap[1]
            # for i in range(2):
            #     heapq.heappop(maxHeap)
            if x < y:
                heapq.heappush(maxHeap, -(y - x))
            print(maxHeap)
        # if maxHeap:
        #     return -maxHeap[0]
        # else:
        #     return 0
        maxHeap.append(0)
        return -maxHeap[0]
