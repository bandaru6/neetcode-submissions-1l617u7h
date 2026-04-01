class MovingAverage:

    def __init__(self, size: int):
        self.nums = []
        self.cap = size

    def next(self, val: int) -> float:
        while len(self.nums) >= self.cap:
            self.nums.pop(0)
        self.nums.append(val)
        return sum(self.nums)/len(self.nums)
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
