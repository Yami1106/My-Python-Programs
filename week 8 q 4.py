import threading

class NumberPrinter:
    def __init__(self, n):
        self.n = n
        self.current_number = 1
        self.lock = threading.Lock()
        self.condition = threading.Condition(self.lock)

    def print_odd(self):
        while self.current_number <= self.n:
            with self.lock:
                if self.current_number % 2 == 0:
                    self.condition.wait()
                print(f"Thread 1: {self.current_number}")
                self.current_number += 1
                self.condition.notify()

    def print_even(self):
        while self.current_number <= self.n:
            with self.lock:
                if self.current_number % 2 == 1:
                    self.condition.wait()
                print(f"Thread 2: {self.current_number}")
                self.current_number += 1
                self.condition.notify()

if __name__ == '__main__':
    printer = NumberPrinter(10)
    t1 = threading.Thread(target=printer.print_odd)
    t2 = threading.Thread(target=printer.print_even)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
