import threading

def work():
    print("Working...")

t = threading.Thread(target = work)
t.start()
t.join()

