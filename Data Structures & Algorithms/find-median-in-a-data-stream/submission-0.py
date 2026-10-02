class MedianFinder:

    def __init__(self):
        self.stream = []

    def addNum(self, num: int) -> None:
        self.stream.append(num)
        

    def findMedian(self) -> float:
        self.stream.sort()
        m = (len(self.stream) // 2)

        if len(self.stream) % 2 == 0:
            return (self.stream[m] + self.stream[m-1]) / 2
        else:
            return self.stream[m]

        