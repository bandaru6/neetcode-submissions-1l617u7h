class MovingAverage:

    def __init__(self, size: int):
        self.data = []
        self.size = size

    def next(self, val: int) -> float:
        self.data.append(val)
        while len(self.data) > self.size:
            self.data.pop(0)
        return float(sum(self.data))/len(self.data)
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
