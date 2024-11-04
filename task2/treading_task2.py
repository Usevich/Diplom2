import threading
import queue
import time
import psutil

def calculate_term(k):
    return (-1)**k / (2*k+1)

def calculate_pi_leibniz_threading(start, end, result_queue):
    process = psutil.Process()
    memory_before = process.memory_info().rss

    results = [calculate_term(k) for k in range(start, end)]
    pi = sum(results) * 4

    memory_after = process.memory_info().rss
    result_queue.put((pi, memory_after - memory_before))

def measure_performance(func, args):
    start_time = time.time()
    threads = []
    result_queue = queue.Queue()
    for arg in args:
        thread = threading.Thread(target=func, args=(arg[0], arg[1], result_queue))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    results = [result_queue.get() for _ in range(len(threads))]
    pi, memory_usage = zip(*results)
    end_time = time.time()
    return sum(pi), end_time - start_time, sum(memory_usage) / len(memory_usage) / (1024*1024)

if __name__ == "__main__":
    n = 1000000
    num_threads = 4  # Количество потоков
    chunksize = n // num_threads
    args = [(chunksize * i, chunksize * (i + 1)) for i in range(num_threads)]

    pi_threading, process_time, process_memory = measure_performance(calculate_pi_leibniz_threading, args)
    with open('threading_task2.log','a') as file:
        file.write(f'{process_time:.2f},{process_memory:.2f}\n')
    print(f"Pi (threading Leibniz): {pi_threading}, время: {process_time:.2f} сек, память: {process_memory:.2f} МБ")