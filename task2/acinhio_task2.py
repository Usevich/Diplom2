import asyncio
import time
import psutil

async def calculate_term(k):
    return (-1)**k / (2*k+1)

async def calculate_pi_leibniz_async(n):
    process = psutil.Process()
    memory_before = process.memory_info().rss

    tasks = [asyncio.create_task(calculate_term(k)) for k in range(n)]
    results = await asyncio.gather(*tasks)
    pi = sum(results) * 4

    memory_after = process.memory_info().rss
    return pi, memory_after - memory_before

def measure_performance(func, *args):
    start_time = time.time()
    result, memory_usage = func(*args)
    end_time = time.time()
    process_time = end_time - start_time
    return result, process_time, memory_usage/(1024*1024)

if __name__ == "__main__":
    n = 1000000
    pi_async, process_time, process_memory = measure_performance(asyncio.run, calculate_pi_leibniz_async(n))
    with open('acinhio_task2.log','a') as file:
        file.write(f'{process_time:.2f},{process_memory:.2f}\n')

    print(f"Pi (async Leibniz): {pi_async}, время: {process_time:.2f} сек, память: {process_memory:.2f} Мбайт")
