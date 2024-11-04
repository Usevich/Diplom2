import requests
import multiprocessing
import time
import psutil

def fetch(url):
    response = requests.get(url)
    #print(response.text[:20])

def main():
    url = 'https://urban-university.ru'
    start_time = time.time()
    process = psutil.Process()
    memory_before = process.memory_info().rss

    with multiprocessing.Pool() as pool:
        results = pool.map(fetch, [url] * 50)

    memory_after = process.memory_info().rss
    end_time = time.time()
    process_time = end_time - start_time
    process_memory = (memory_after - memory_before)/(1024*1024)


    print(f"Время выполнения: {end_time - start_time} секунд")
    print(f"Использование памяти: {(memory_after - memory_before)/(1024*1024)} Мбайт")
    with open('multiprocessing_task1.log','a') as file:
        file.write(f'{process_time:.2f},{process_memory:.2f}\n')
    return process_time, process_memory
if __name__ == "__main__":
    main()