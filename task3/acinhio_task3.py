import asyncio
import time
import psutil

async def calculate_term(k):
    time.sleep(0.1)
    return k

async def calculate(n):
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
    n = 100
    pi_async, process_time, process_memory = measure_performance(asyncio.run, calculate(n))
    with open('acinhio_task3.log','a') as file:
        file.write(f'{process_time:.2f},{process_memory:.2f}\n')

    print(f"Pi (async Leibniz): {pi_async}, время: {process_time:.2f} сек, память: {process_memory:.2f} Мбайт")
