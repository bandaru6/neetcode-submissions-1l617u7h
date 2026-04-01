class Logger:

    def __init__(self):
        self.data = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:

        if message not in self.data:
            self.data[message] = timestamp
        else:
            if timestamp - self.data[message] < 10:
                return False
            else:
                self.data[message] = timestamp
        
        return True


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
