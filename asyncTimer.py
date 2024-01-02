import threading
import time


class AsyncTimer(threading.Thread):
    def __init__(self, currentTime, game):
        threading.Thread.__init__(self)
        self.startTime = time.time()
        self.endTime = 0
        self.currentTime = currentTime
        self.game = game

    def run(self):
        while True:
            if not self.game.running:
                break
            self.endTime = time.time()
            self.currentTime += self.endTime - self.startTime
            print(self.currentTime)
            self.startTime = time.time()
