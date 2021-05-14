import threading
import time


def func(nr):
    time.sleep(3)
    print("Finished execution from thread {}".format(nr))


time_start = time.time()
threads = set()

for i in range(1, 6):
    t = threading.Thread(target=func, args=(i,))
    t.start()

    print('Thread {} alive status: {}'.format(t.name, t.is_alive()))

    count = threading.active_count()
    print("Total no of threads: {}".format(count))

    threads.add(t)

for thread in threads:
    thread.join()

time_end = time.time()
total_time = time_end - time_start
print(f'Total time: {total_time:.10f}')