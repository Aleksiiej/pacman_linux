import threading
import time
import pygame


class AsyncScatterTimer(threading.Thread):
    def __init__(self, game):
        threading.Thread.__init__(self)
        self.startTime_ = time.time()
        self.endTime_ = 0
        self.currentTime_ = 0
        self.game_ = game

    def run(self):
        while True:
            if not self.game_.running_:
                break
            self.endTime_ = time.time()
            self.currentTime_ += self.endTime_ - self.startTime_
            self.startTime_ = time.time()
            pygame.time.delay(100)
