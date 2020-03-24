from time import perf_counter as counter
import numpy as np


class Timer:
    def __init__(self, length):
        self.length = length
        self.progresses = {int(self.length // (100 / i)): i for i in range(1, 101, 1)}
        self.durations = np.array([])
        self.t0 = None
        self.t1 = None

    def time_check(self, idx):
        if idx == 0:
            self.t0 = counter()
            if idx in self.progresses:
                print("WARNING: The length is to small for this timer.")
        elif idx in self.progresses:
            self.t1 = counter()
            duration = self.t1 - self.t0
            self.t0 = counter()
            self.durations = np.append(self.durations, duration)
            elapsed = self.durations.sum()
            idx = 1 if idx == 0 else idx
            eta = elapsed * ((self.length / idx) - 1)
            self.print_time(idx, elapsed, eta)
        else:
            pass

    def print_time(self, idx, elapsed, eta):
        percent = "{:^2}%".format(self.progresses[idx])
        print(percent, end='  |  ')
        if elapsed > 60:
            print("Elapsed: {:^5.2f} min".format(elapsed / 60), end='  |  ')
        else:
            print("Elapsed: {:^5.2f} sec".format(elapsed), end='  |  ')
        if eta > 60:
            print('ETA: {:^5.2f} min'.format(eta / 60))
        else:
            print('ETA: {:^5.2f} sec'.format(eta))
