# basics Example of multithreading in Python
import threading
import time


def task(name):
    print(f"Thread {name} starting")
    time.sleep(2)
    print(f"Thread {name} finished")


thread1 = threading.Thread(target=task, args=("Task A",))
thread2 = threading.Thread(target=task, args=("Task B",))

thread1.start()
thread2.start()

thread1.join() # its a blocking call, it will wait for thread1 to finish before moving on to the next line of code
thread2.join()

print("Both threads have finished execution.")
