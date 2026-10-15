class Twitter:

    def __init__(self):
        self.time = 0
        self.tweetMap = defaultdict(list) # maps userId to a list of [time, tweetId]
        self.followMap = defaultdict(set) # maps userId to who they follow
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.time, tweetId])
        self.time += 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        maxHeap = []

        self.followMap[userId].add(userId)
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap: #checks if they have a tweet
                index = len(self.tweetMap[followeeId]) - 1
                time, tweetId = self.tweetMap[followeeId][index]
                maxHeap.append([time, tweetId, followeeId, index-1]) #index-1 points to the next position to search
        heapq.heapify_max(maxHeap)

        while len(res) < 10 and maxHeap:
            time, tweetId, followeeId, index = heapq.heappop_max(maxHeap)
            res.append(tweetId)
            if index >= 0:
                time, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush_max(maxHeap, [time, tweetId, followeeId, index-1])
        
        return res

        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
        

        



        
