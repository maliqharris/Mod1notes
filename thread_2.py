import threading 
def work(task_id):
    print(f"Tread {task_id} is working...")

# Create multiple threads
threads = []
for i in range(5):
    t = threading.Thread(target=work, args=(i,))
    threads.append(t)
    t.start()

# Wait for all threads to complete
for t in threads:
    t.join()

print("All threads have completed their work.")