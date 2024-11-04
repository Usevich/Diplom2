import multiprocessing
import time
import psutil


def calculate_term(k):
    time.sleep(0.1)
    return k


def calculate(start, end):
    process = psutil.Process()
    memory_before = process.memory_info().rss

    results = [calculate_term(k) for k in range(start, end)]
    pi = sum(results) * 4

    memory_after = process.memory_info().rss
    return pi, memory_after - memory_before


def measure_performance(func, args):
    start_time = time.time()
    with multiprocessing.Pool() as pool:
        results = pool.starmap(func, args)
        pi, memory_usage = zip(*results)
    end_time = time.time()
    return sum(pi), end_time - start_time, sum(memory_usage)/(1024*1024)


if __name__ == "__main__":
    n = 100
    num_processes = 4  # Количество процессов
    chunksize = n // num_processes
    args = [(chunksize * i, chunksize * (i + 1)) for i in range(num_processes)]

    pi_mp, process_time, process_memory = measure_performance(calculate, args)
    with open('multiprocessing_task3.log','a') as file:
        file.write(f'{process_time:.2f},{process_memory:.2f}\n')
    print(f"Pi (multiprocessing Leibniz): {pi_mp}, время: {process_time:.2f} сек, память: {process_memory:.2f} МБ")
