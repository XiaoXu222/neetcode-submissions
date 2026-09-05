class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = {}
        for task in tasks:
            if task not in freq:
                freq[task] = 1
            else:
                freq[task] += 1
        freqList = [-value for value in freq.values()]
        heapq.heapify(freqList)
        cool = deque()
        time = 0
        while freqList or cool:
            time += 1
            if not freqList:
                time = cool[0][1]
            else:
                frequency = heapq.heappop(freqList) + 1
                if frequency < 0:
                    cool.append([frequency, time + n])
            if cool and cool[0][1] == time:
                left = cool.popleft()
                heapq.heappush(freqList, left[0])
        return time
            



        