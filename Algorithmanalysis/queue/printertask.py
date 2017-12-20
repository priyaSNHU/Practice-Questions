class printer:
    def __init__(self, ppm):
        self.page_rate = ppm
        self.current_task = None
        self.time_remaining = 0
    def tick(self):
        if self.current_task != None:
            self.remaining_time = self.remaining_time -1
            if self.remaining_time == 0:
                self.current_task = None
    def busy(self):
        if self.current_task != None:
            return True
        else:
            return False
    def next_task(self, new_task):
        self.current_task = new_task
        self.time_remaining = new_task.get_pages() * 60 / self.page_rate
