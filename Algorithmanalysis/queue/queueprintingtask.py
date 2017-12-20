from classqueue import Queue
import random

class printer:
    def __init__(self, ppm):
        self.page_rate = ppm
        self.current_task = None
        self.time_remaining = 0
    def tick(self):
        if self.current_task != None:
            self.time_remaining = self.time_remaining -1
            if self.time_remaining == 0:
                self.current_task = None
    def busy(self):
        if self.current_task != None:
            return True
        else:
            return False
    def next_task(self, new_task):
        self.current_task = new_task
        self.time_remaining = new_task.get_pages() * 60 / self.page_rate
    
    
class task:

    def __init__(self, time):
        self.timestamp = time
        self.pages = random.randrange(1,21)

    def get_stamp(self):
        return self.timestamp

    def get_pages(self):
        return self.pages

    def wait_time(self, current_time):
        return current_time - self.timestamp

def simulation(num_seconds, pages_per_minute):
    lab_printer = printer(pages_per_minute)
    print_queue = Queue()
    waiting_time = []
    for sec in range(num_seconds):
        if new_print_task():
            ntask = task(sec)
            print_queue.enqueue(ntask)
        if (not lab_printer.busy() ) and (not print_queue.is_empty()):
            next_task = print_queue.dequeue()
            waiting_time.append(next_task.wait_time(sec))
            lab_printer.next_task(next_task)
        lab_printer.tick()

    avg_wait = sum(waiting_time) / len (waiting_time)
    print("Average wait %6.2f secs %3d tasks remaining." %(avg_wait, print_queue.size()))

def new_print_task():
    num = random.randrange(1,181)
    if num == 180:
        return True
    else:
        return False

for i in range(10):
    simulation(3600,5)
            
        
