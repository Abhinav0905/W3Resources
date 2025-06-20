import queue
import threading

class ThreadSafePriorityQueue:

    def __init__(self):
        self._queue = queue.PriorityQueue()
        self._lock = threading.Lock()

    # method to put an inten into the priority queue
    def _put(self, item, priority):
        with self._lock:
            self._queue._put((priority, item))

    # Method to get an item from the priority queue

    def get(self):

        with self._lock:
            if not self._queue.empty():
                priority , item = self._queue.get()
                return item
            else:
                return None


if __name__ == "__main__":

    def producer(q):
        for i in range(5):
            q.put(i,i)

