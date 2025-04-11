from threading import Event, Thread
import time

event = Event()

def wait_event():
    print("Waiting for event...")
    event.wait()
    print("Event received!")

t = Thread(target=wait_event)
t.start()
time.sleep(2)
print("Setting event")
event.set()
