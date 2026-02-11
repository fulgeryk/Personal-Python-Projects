import time
from math import ceil


class Engine:
    def __init__(self):
        self.timeout_s = 5
        self.remaining_s = None
        self.is_running = False
        self.last_activity = None

    def on_activity(self):
        current_time = time.monotonic()
        self.last_activity = current_time
        self.is_running = True

    def tick(self):
        if self.is_running and self.last_activity is not None:
            current = time.monotonic()
            elapsed = current - self.last_activity
            self.remaining_s = self.timeout_s - elapsed
            self.remaining_s = ceil(self.remaining_s)
            if self.remaining_s <= 0:
                self.is_running = False
                self.last_activity = None
                return 0, True
            else:
                return self.remaining_s, False
        else:
            return None, False

    def set_idle(self):
        self.remaining_s = None
        self.is_running = False