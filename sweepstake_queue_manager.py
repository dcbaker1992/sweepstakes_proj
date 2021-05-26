from queue_data import Queue


class SweepstakesQueueManager:
    def __init__(self):
        self.queue = Queue()

    def insert_sweepstakes(self, sweepstake):
        pass

    def get_sweepstakes(self):
        return self.queue.dequeue()
