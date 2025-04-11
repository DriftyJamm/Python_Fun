from threading import Thread, Lock

lock = Lock()
count = 0

def increment():
    global count
    with lock:
        for _ in range(1000):
            count += 1

t1 = Thread(target=increment)
t2 = Thread(target=increment)
t1.start()
t2.start()
t1.join()
t2.join()

print("Final count:", count)
