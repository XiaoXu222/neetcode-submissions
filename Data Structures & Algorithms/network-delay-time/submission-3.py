class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = {}
        for i in range(n):
            graph[i+1] = []
        for ui, vi, ti in times:
            graph[ui].append([vi, ti])
        
        receive = {}
        minHeap = [[0, k]]

        while minHeap:
            tc, nc = heapq.heappop(minHeap)
            if nc in receive:
                continue
            receive[nc] = tc

            for nn, tn in graph[nc]:
                if nn not in receive:
                    heapq.heappush(minHeap, [tc + tn, nn])
        if len(receive) < n:
            return -1
        else:
            return max(receive.values())

