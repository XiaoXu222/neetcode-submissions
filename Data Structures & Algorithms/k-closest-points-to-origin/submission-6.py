class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for point in points:
            distance = point[0]**2 + point[1]**2
            heapq.heappush(heap, (-distance, -point[0], -point[1]))
            if len(heap) > k:
                heapq.heappop(heap)
        res = []
        for i in heap:
            res.append([-i[1], -i[2]])
        return res

