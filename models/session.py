class Session():
    def __init__(self, name, time, date, duration, capacity, id=None):
        self.name = name
        self.time = time
        self.date = date
        self.duration = duration
        self.capacity = capacity
        self.id = id 