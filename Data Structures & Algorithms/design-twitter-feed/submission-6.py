class Twitter:

    def __init__(self):
        self.time = 0
        self.tweetMap = {}
        self.followMap = {}
    
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        if userId not in self.tweetMap:
            self.tweetMap[userId] = deque([[self.time, tweetId]])
        else:
            self.tweetMap[userId].append([self.time, tweetId])
            if len(self.tweetMap[userId]) > 10:
                self.tweetMap[userId].popleft()


    def getNewsFeed(self, userId: int) -> List[int]:
        if userId not in self.followMap and userId in self.tweetMap:
            self.followMap[userId] = set()
        elif userId in self.followMap and userId not in self.tweetMap:
            self.tweetMap[userId] = deque()
        elif userId not in self.followMap and userId not in self.tweetMap:
            return []
        mergeList = self.followMap[userId].copy()
        mergeList.add(userId)
        minHeap = []
        heapq.heapify(minHeap)
        for pp in mergeList:
            if pp not in self.tweetMap:
                continue
            tweets = self.tweetMap[pp]
            for j in range(len(tweets)):
                heapq.heappush(minHeap, tweets[j])
                if len(minHeap) > 10:
                    heapq.heappop(minHeap)
        resInv = []
        for n in range(len(minHeap)):
            resInv.append(heapq.heappop(minHeap)[1])
        res = []
        for k in range(len(resInv) - 1, -1, -1):
            res.append(resInv[k])
        return res
       
    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followMap:
            self.followMap[followerId] = set([followeeId])
        else:
            self.followMap[followerId].add(followeeId)

        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followMap:
            if followeeId in self.followMap[followerId]:
                self.followMap[followerId].remove(followeeId)

        
