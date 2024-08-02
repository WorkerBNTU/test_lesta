# 1 реализация
class CircularBufferFIFO:
    def __init__(self, max_size):
        self.max_size = max_size
        self.buffer = []

    def add(self, item):
        if len(self.buffer) == self.max_size:
            self.buffer.pop(0)
        self.buffer.append(item)

    def pop(self):
        if self.buffer:
            return self.buffer.pop(0)
        return None


# 2 реализация
class CircularBufferFIFO2:
    def __init__(self, size):
        self.size = size
        self.buffer = [None] * size
        self.start = 0
        self.end = -1

    def add(self, item):
        self.end = (self.end + 1) % self.size
        self.buffer[self.end] = item
        if self.end == self.start:
            self.start = (self.start + 1) % self.size

    def get(self):
        return self.buffer[self.start]


# 3 реализация
class CircularBufferFIFO3:
    def __init__(self, max_size: int):
        self.max_size = max_size
        self.buffer = deque([], maxlen=max_size)

    def is_empty(self) -> bool:
        return len(self.buffer) == 0

    def is_full(self) -> bool:
        return len(self.buffer) == self.max_size

    def add(self, value):
        if self.is_full():
            self.buffer.popleft()
        self.buffer.append(value)

    def pop(self):
        if self.is_empty():
            return 'empty'
        return self.buffer.popleft()
