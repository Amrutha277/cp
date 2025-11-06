# Last updated: 11/5/2025, 10:36:21 PM
class Logger:

    def __init__(self):
        self.msg_time= {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.msg_time:
            self.msg_time[message] = timestamp
            return True

        last_seen= self.msg_time[message]
        if timestamp -last_seen >= 10:
            self.msg_time[message] = timestamp
            return True
        return False

        

        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)