import threading
import time
import pygame


class AsyncTimer(threading.Thread):
    def __init__(self, game):
        threading.Thread.__init__(self)
        self.startTime = time.time()
        self.endTime = 0
        self.currentTime = 0
        self.game = game

    def run(self):
        while True:
            if not self.game.running:
                break
            self.endTime = time.time()
            self.currentTime += self.endTime - self.startTime
            self.startTime = time.time()
            pygame.time.delay(100)
