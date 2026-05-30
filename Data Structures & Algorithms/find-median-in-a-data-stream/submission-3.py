from _heapq import heapify
class MedianFinder:

    def __init__(self):
        self.heap1 = []
        self.heap2 = []
        self.numOfElems = 0
        

    def addNum(self, num: int) -> None:
        heapq.heappush_max(self.heap1, num)
        if (self.heap1 and self.heap2 and self.heap1[0] > self.heap2[0]):
            val = heapq.heappop_max(self.heap1)
            heapq.heappush(self.heap2, val)
        if len(self.heap1) - len(self.heap2) > 1:
            val = heapq.heappop_max(self.heap1)
            heapq.heappush(self.heap2, val)
        if len(self.heap2) - len(self.heap1) > 1:
            val = heapq.heappop(self.heap2)
            heapq.heappush_max(self.heap1, val)
        #heapq.heappush(self.heap2, num)
        self.numOfElems += 1

    def findMedian(self) -> float:
        print("HEAP 1", self.heap1)
        print("HEAP 2",self.heap2)
        if self.numOfElems % 2 == 1:
            if len(self.heap1) > len(self.heap2):
                return self.heap1[0]
            else:
                return self.heap2[0]
        if self.numOfElems == 0:
            return 0
        #print(self.root)
        return (self.heap1[0] + self.heap2[0]) / 2
        