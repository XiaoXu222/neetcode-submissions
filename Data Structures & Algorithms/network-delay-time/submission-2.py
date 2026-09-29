class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {}
        for i in range(n):
            adj[i + 1] = []
        for s, d, w in times:
            adj[s].append([d, w])
        
        minTime = {}
        res = 0
        minHeap = [(0, k)]
        while minHeap:
            t, node = heapq.heappop(minHeap)
            if node in minTime:
                continue
            minTime[node] = t
            res = t

            for dn, wn in adj[node]:
                if dn in minTime:
                    continue
                heapq.heappush(minHeap, [(t + wn), dn])

        if len(minTime) == n:
            return res
        else:
            return -1
