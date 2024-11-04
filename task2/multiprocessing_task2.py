import multiprocessing
import time
import psutil


def calculate_term(k):
    return (-1) ** k / (2 * k + 1)


def calculate_pi_leibniz_mp( start, end):
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
    n = 1000000
    num_processes = 4  # Количество процессов
    chunksize = n // num_processes
    args = [(chunksize * i, chunksize * (i + 1)) for i in range(num_processes)]

    pi_mp, process_time, process_memory = measure_performance(calculate_pi_leibniz_mp, args)
    with open('multiprocessing_task2.log','a') as file:
        file.write(f'{process_time:.2f},{process_memory:.2f}\n')
    print(f"Pi (multiprocessing Leibniz): {pi_mp}, время: {process_time:.2f} сек, память: {process_memory:.2f} МБ")
